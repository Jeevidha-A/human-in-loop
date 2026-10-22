
def generate_email(reason, leave_date):
    """Generate a leave email using a template."""

    subject = f"Leave Request - {leave_date}"

    content = (
        f"I would like to request leave on {leave_date} "
        f"due to {reason}. Kindly approve my request."
    )

    return subject, content


def revise_email(content, instruction):
    """Revise the email using simple rules."""

    instruction = instruction.lower()

    if "short" in instruction:
        return "I request leave due to the mentioned reason. Please approve."

    elif "polite" in instruction:
        return (
            content.replace(
                "Kindly approve my request.",
                "I would appreciate your approval."
            )
        )

    elif "formal" in instruction:
        return (
            "I am writing to request leave. "
            + content
        )

    else:
        print("Instruction not supported.")
        print("Try: shorter, polite, or formal.")
        return content


def main():
    print("\n=== Simple Human-in-the-Loop Agent ===")

    reason = input("Enter your leave reason: ")
    leave_date = input("Enter your leave date: ")

    subject, content = generate_email(reason, leave_date)

    while True:
        print("\n--- Generated Email ---")
        print("Subject:", subject)
        print("Content:", content)

        print("\nChoose an action:")
        print("1. Revise email")
        print("2. Approve email")
        print("3. Reject email")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            instruction = input(
                "How do you want to revise it? "
            )
            content = revise_email(content, instruction)

        elif choice == "2":
            print("\nEmail approved by human reviewer.")
            print("The email has been sent.")
            break

        elif choice == "3":
            print("\nEmail rejected.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
