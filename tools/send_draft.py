from collections.abc import Generator
from typing import Any

import requests
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage


class SendDraftTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        try:
            # Get parameters
            draft_id = tool_parameters.get("draft_id")
            
            if not draft_id:
                yield self.create_text_message("Error: Draft ID is required.")
                return
            
            # Get credentials from tool provider
            access_token = self.runtime.credentials.get("access_token")
            
            if not access_token:
                yield self.create_text_message("Error: No access token available. Please authorize the Gmail integration.")
                return
            
            headers = {
                "Authorization": f"Bearer {access_token}",
                "Accept": "application/json"
            }
            
            yield self.create_text_message(f"Sending draft {draft_id}...")
            
            # Send the draft
            send_url = f"https://gmail.googleapis.com/gmail/v1/users/me/drafts/{draft_id}/send"
            
            response = requests.post(
                send_url,
                headers=headers,
                timeout=30
            )
            
            if response.status_code == 401:
                yield self.create_text_message("Error: Access token expired. Please re-authorize the Gmail integration.")
                return
            elif response.status_code == 404:
                yield self.create_text_message("Error: Draft not found. The draft ID may be invalid or the draft may have been deleted.")
                return
            elif response.status_code != 200:
                yield self.create_text_message(f"Error: Gmail API returned status {response.status_code}: {response.text}")
                return
            
            # Parse response
            response_data = response.json()
            message_id = response_data.get("id")
            thread_id = response_data.get("threadId")
            
            if not message_id:
                yield self.create_text_message("Error: Failed to send draft. No message ID received.")
                return
            
            # Return success results
            yield self.create_text_message("Draft sent successfully!")
            yield self.create_json_message({
                "status": "success",
                "draft_id": draft_id,
                "message_id": message_id,
                "thread_id": thread_id
            })
            
        except requests.RequestException as e:
            yield self.create_text_message(f"Network error: {str(e)}")
        except Exception as e:
            yield self.create_text_message(f"Error sending draft: {str(e)}") 