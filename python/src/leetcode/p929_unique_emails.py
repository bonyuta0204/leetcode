from typing import List,  Optional

class Solution:
    def numUniqueEmails(self,  emails: List[str]) -> int:
        """
        we transform each emails to regularized email.
        then we put the email in to set and see the length of set
        """

        uniq_emails = set()

        for email in emails:
            regularize_email = self.regularizeEmail(email)

            print(f"{regularize_email =}")

            if regularize_email is not None and regularize_email not in uniq_emails:
                uniq_emails.add(regularize_email)

        return len(uniq_emails)

    def regularizeEmail(self,  email: str) -> Optional[str]:
        """
        we first split the email to local and domain then transform localpart
        """

        splited = email.split("@")

        if len(splited) != 2:
            return None

        local = splited[0]
        domain = splited[1]

        local = local.lower()
        local = "".join([c for c  in local if c != "." ]) # remove .
        local = local.split("+")[0]

        return f"{local}@{domain}"
