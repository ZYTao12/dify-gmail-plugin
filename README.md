# Gmail Plugin for Dify

A comprehensive Gmail integration plugin for Dify that provides essential mail-related actions using OAuth2.0 authentication.

## Features

This plugin extends beyond the basic "read emails" functionality to provide a comprehensive set of Gmail management capabilities:

### 📧 **Email Management**
- **List Messages**: List emails from various Gmail folders (inbox, sent, drafts, spam, trash, custom labels)
- **Get Message Details**: Retrieve detailed information about specific emails including headers, body, and attachments
- **Search Messages**: Advanced Gmail search using Gmail's powerful search syntax and operators

### ✉️ **Email Composition & Sending**
- **Send Message**: Send emails directly with recipients, subject, body, CC, BCC, and reply-to
- **Create Drafts**: Create draft emails that can be edited and sent later
- **List Drafts**: View and manage draft emails
- **Send Drafts**: Send previously created draft emails

### 📎 **Attachment Support**
- **Add Attachments**: Attach files to draft emails (supports files up to 25MB)

### 🏷️ **Email Organization**
- **Flag Messages**: Mark emails for follow-up using Gmail's starring system
- **Advanced Filtering**: Use Gmail search operators for precise email filtering

## Gmail Search Operators

The plugin supports Gmail's powerful search syntax:

- **Sender/Recipient**: `from:example@gmail.com`, `to:colleague@company.com`
- **Subject**: `subject:meeting`, `subject:"project update"`
- **Date Ranges**: `after:2024/01/01`, `before:2024/12/31`
- **Status**: `is:unread`, `is:read`, `is:starred`, `is:important`
- **Attachments**: `has:attachment`, `filename:pdf`
- **Size**: `larger:10M`, `smaller:1M`
- **Labels**: `label:work`, `label:personal`
- **Combined**: `from:boss@company.com subject:meeting after:2024/01/01 has:attachment`

## Setup Instructions

### 1. Google Cloud Console Setup

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the Gmail API:
   - Go to "APIs & Services" > "Library"
   - Search for "Gmail API" and enable it

### 2. Create OAuth 2.0 Credentials

1. Go to "APIs & Services" > "Credentials"
2. Click "Create Credentials" > "OAuth 2.0 Client IDs"
3. Choose "Desktop application" as the application type
4. Download the credentials JSON file
5. Note your **Client ID** and **Client Secret**

### 3. Configure the Plugin

1. In Dify, add the Gmail plugin
2. Enter your **Client ID** and **Client Secret**
3. Complete the OAuth2.0 authorization flow
4. The plugin will request the following scopes:
   - `https://www.googleapis.com/auth/gmail.readonly` - Read emails
   - `https://www.googleapis.com/auth/gmail.send` - Send emails
   - `https://www.googleapis.com/auth/gmail.compose` - Create drafts
   - `https://www.googleapis.com/auth/gmail.modify` - Modify emails
   - `https://www.googleapis.com/auth/gmail.labels` - Manage labels
   - `https://www.googleapis.com/auth/gmail.metadata` - Read metadata

## Usage Examples

### List Recent Inbox Messages
```yaml
tool: list_messages
parameters:
  folder: inbox
  limit: 10
  include_body: false
```

### Search for Important Emails
```yaml
tool: search_messages
parameters:
  query: "is:important subject:urgent after:2024/01/01"
  max_results: 20
  include_body: true
```

### Send an Email
```yaml
tool: send_message
parameters:
  to: "recipient@example.com"
  subject: "Meeting Reminder"
  body: "Hi, this is a reminder about our meeting tomorrow."
  cc: "manager@example.com"
```

### Create a Draft
```yaml
tool: draft_message
parameters:
  to: "team@company.com"
  subject: "Weekly Update"
  body: "Here's our weekly team update..."
```

### Flag a Message for Follow-up
```yaml
tool: flag_message
parameters:
  message_id: "18c1a2b3d4e5f6g7"
  action: "flag"
```

## Tool Reference

### Core Tools

| Tool | Description | Key Parameters |
|------|-------------|----------------|
| `list_messages` | List emails from Gmail folders | `folder`, `limit`, `search_query`, `include_body` |
| `get_message` | Get detailed message information | `message_id`, `include_body`, `include_attachments` |
| `search_messages` | Advanced Gmail search | `query`, `max_results`, `include_body`, `sort_by` |

### Email Composition

| Tool | Description | Key Parameters |
|------|-------------|----------------|
| `send_message` | Send email immediately | `to`, `subject`, `body`, `cc`, `bcc`, `reply_to` |
| `draft_message` | Create draft email | `to`, `subject`, `body`, `cc`, `bcc`, `reply_to` |
| `list_drafts` | List draft emails | `limit`, `include_body`, `search_query` |
| `send_draft` | Send draft email | `draft_id` |

### Advanced Features

| Tool | Description | Key Parameters |
|------|-------------|----------------|
| `add_attachment_to_draft` | Add file to draft | `draft_id`, `file_path`, `attachment_name` |
| `flag_message` | Flag/unflag for follow-up | `message_id`, `action` |

## Error Handling

The plugin provides comprehensive error handling:

- **Authentication Errors**: Clear messages when OAuth tokens expire
- **API Errors**: Detailed error messages from Gmail API
- **Validation Errors**: Parameter validation with helpful suggestions
- **File Errors**: Clear messages for file access and size issues

## Limitations

- **File Attachments**: Maximum 25MB per file (Gmail API limitation)
- **Rate Limits**: Subject to Gmail API rate limits
- **Authentication**: Requires OAuth2.0 setup and periodic token refresh

## Troubleshooting

### Common Issues

1. **"Access token expired"**: Re-authorize the plugin in Dify
2. **"File not found"**: Ensure the file path is accessible from the plugin environment
3. **"Draft not found"**: Verify the draft ID is valid and hasn't been deleted
4. **"Permission denied"**: Check that all required Gmail scopes are granted

### Getting Help

- Check the Gmail API documentation for detailed error codes
- Verify your OAuth2.0 credentials are correct
- Ensure the Gmail API is enabled in your Google Cloud project

## Development

This plugin is built using the Dify plugin framework and follows best practices:

- **Modular Design**: Each tool is implemented as a separate class
- **Error Handling**: Comprehensive error handling and user feedback
- **Progress Updates**: Real-time progress updates for long-running operations
- **Internationalization**: Multi-language support for labels and descriptions

## License

This plugin is provided as-is for use with Dify. Please refer to Dify's licensing terms for usage rights. 