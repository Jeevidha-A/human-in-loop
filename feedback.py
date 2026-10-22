
def generate_email(reason, leave_date):
    subject = f"Leave Request - {leave_date}"

    content = (
        f"I would like to request leave on {leave_date} "
        f"due to {reason}. Kindly approve my request."
    )

    return subject, content


def improve_email(content, feedback):
    feedback = feedback.lower()

    # Improve the email based on user feedback
    if "shorter" in feedback or "short" in feedback:
        content = (
            "I request leave on the specified date "
            "due to the mentioned reason. Please approve."
        )

    elif "polite" in feedback:
        content = content.replace(
            "Kindly approve my request.",
            "I would appreciate your approval."
        )

    elif "formal" in feedback:
        content = (
            "I am writing to request leave. " + content
        )

    else:
        print("Feedback not recognized.")
        print("Try: make it shorter, polite, or formal.")

    return content


def main():
    print("=== Feedback-in-the-Loop Agent ===")

    reason = input("Enter your leave reason: ")
    leave_date = input("Enter your leave date: ")

    subject, content = generate_email(reason, leave_date)

    # Continue until the user accepts the email
    while True:
        print("\n--- Current Email ---")
        print("Subject:", subject)
        print("Content:", content)

        print("\n1. Give feedback")
        print("2. Accept email")

        choice = input("Enter your choice (1/2): ")

        if choice == "1":
            feedback = input(
                "What should be improved? "
            )

            content = improve_email(content, feedback)

            print("\nEmail updated using your feedback.")

        elif choice == "2":
            with open("final_email.txt", "w") as file:
                file.write(f"Subject: {subject}\n\n")
                file.write(f"Content: {content}\n")

            print("\nEmail accepted!")
            print("Saved to final_email.txt")
            break

        else:
            print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
