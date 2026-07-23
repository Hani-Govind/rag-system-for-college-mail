import json


relevant_keywords = [

    "hackathon",
    "workshop",
    "internship",
    "placement",
    "research",
    "competition",
    "seminar",
    "conference",
    "registration",
    "opportunity",
    "event",
    "training",
    "bootcamp",
    "scholarship",
    "industrial visit",
    "project",
    "paper presentation",
    "coding"

]


# opening the dataset

with open(
        "emails.json",
        "r",
        encoding="utf-8"
) as file:

    emails = json.load(file)



filtered_emails = []


# filtering

for email in emails:

    text = (

        email.get("subject","") +

        " " +

        email.get("snippet","")

    ).lower()


    for keyword in relevant_keywords:

        if keyword in text:

            filtered_emails.append(email)
            break



# storing the filtered dataset

with open(

        "extracted_emails/filtered_emails.json",
        "w",
        encoding="utf-8"

) as file:


    json.dump(

        filtered_emails,
        file,
        indent=4,
        ensure_ascii=False

    )



print("\nFiltering Completed Successfully!")

print(f"\nOriginal Dataset : {len(emails)}")

print(f"Filtered Dataset : {len(filtered_emails)}")