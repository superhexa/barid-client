import asyncio
from barid.client import BaridClient
from barid.types import EmailAddress, EmailId

async def main():
    email = EmailAddress("example@barid.site")

    async with BaridClient() as client:
        domains = await client.get_domains()
        print("Available Domains:", domains)

        total = await client.count_emails(email=email)
        print("Total Emails:", total)

        emails = await client.get_emails(email=email, limit=5)
        print(f"\nFetched {len(emails)} email(s)\n")

        for msg in emails:
            print("Subject:", msg.subject)

            details = await client.get_email(email_id=EmailId(msg.id))
            print(details)
            print("Content:", details.text_content or details.html_content)
            print()

        if emails:
            await client.delete_email(email_id=EmailId(emails[0].id))
            print("Deleted the latest email")

        await client.delete_emails(email=email)
        print("Deleted all emails")

asyncio.run(main())
