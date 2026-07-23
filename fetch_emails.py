from main import service
import json

# stores all extracted emails
email_dataset = []


# fetching emails
results = service.users().messages().list(
    userId="me",
    maxResults=300
).execute()


messages = results.get("messages", [])

print(f"\nTotal Emails Collected : {len(messages)}")


# loop through all emails
for email in messages:

    email_id = email["id"]

    message = service.users().messages().get(
        userId="me",
        id=email_id
    ).execute()

    # metadata
    subject = ""
    sender = ""
    date = ""

    headers = message["payload"].get("headers", [])

    for item in headers:

        if item["name"] == "Subject":
            subject = item["value"]

        elif item["name"] == "From":
            sender = item["value"]

        elif item["name"] == "Date":
            date = item["value"]


    # snippet of the email
    snippet = message.get("snippet", "")


    # storing the email
    email_data = {

        "subject": subject,
        "sender": sender,
        "date": date,
        "snippet": snippet

    }

    email_dataset.append(email_data)



# checking if extraction worked
print("\nEmails Successfully Extracted :", len(email_dataset))

if len(email_dataset) > 0:
    print("\nSample Email:\n")
    print(email_dataset[0])



# saving the dataset
with open(
    "emails.json",
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        email_dataset,
        file,
        indent=4,
        ensure_ascii=False
    )


print("\nDataset Created Successfully!")
print(f"Total Emails Stored : {len(email_dataset)}")