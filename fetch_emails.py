from main import service


results = service.users().messages().list(
            userId="me",
            maxResults=5
            ).execute()


messages = results.get("messages",[])


print(messages)