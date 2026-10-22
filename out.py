
def generate_email(reason, leave_date):
    subject = f"Leave Request - {leave_date}"

    content = (
        f"I would like to request leave on {leave_date} "
        f"due to {reason}. Kindly approve my request."
    )

    return subject, content


def save_email(subject, content):
    # Save the email automatically
    with open("leave_email.txt", "w") as file:
        file.write(f"Subject: {subject}\n\n")
        file.write(f"Content: {content}\n")

    print("\nEmail generated and saved automatically!")
    print("File name: leave_email.txt")


def main():
    print("=== Human-out-of-the-Loop Agent ===")

    reason = input("Enter your leave reason: ")
    leave_date = input("Enter your leave date: ")

    # Agent generates the email
    subject, content = generate_email(reason, leave_date)

    # Display the result
    print("\n--- Generated Email ---")
    print("Subject:", subject)
    print("Content:", content)

    # Automatically save without human approval
    save_email(subject, content)

    print("Task completed automatically!")


if __name__ == "__main__":
    main()
