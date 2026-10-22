
def generate_email(reason, leave_date):
    subject = f"Leave Request - {leave_date}"

    content = (
        f"I would like to request leave on {leave_date} "
        f"due to {reason}. Kindly approve my request."
    )

    return subject, content


def save_email(subject, content):
    with open("approved_email.txt", "w") as file:
        file.write(f"Subject: {subject}\n\n")
        file.write(f"Content: {content}\n")

    print("\nApproved email saved to approved_email.txt")


def main():
    print("=== Approval-Based Agent ===")

    reason = input("Enter your leave reason: ")
    leave_date = input("Enter your leave date: ")

    # Step 1: Generate email
    subject, content = generate_email(reason, leave_date)

    # Step 2: Display email for review
    print("\n--- Email Preview ---")
    print("Subject:", subject)
    print("Content:", content)

    # Step 3: Ask for human approval
    approval = input("\nApprove this email? (yes/no): ")
    approval = approval.strip().lower()

    # Step 4: Take action based on approval
    if approval == "yes":
        save_email(subject, content)
        print("Task completed successfully!")

    elif approval == "no":
        print("Email rejected. Nothing was saved.")

    else:
        print("Invalid choice. Please enter yes or no.")


if __name__ == "__main__":
    main()
