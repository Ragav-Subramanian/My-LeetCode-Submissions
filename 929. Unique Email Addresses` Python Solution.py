class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ans=set()
        for email in emails:
            flag=False
            email=email.split("@")
            if '.' in email[0]:
                flag=True
            ind=email[0].find("+")
            if ind!=-1:
                email[0]=email[0][:ind]
            if flag:
                email[0]=email[0].replace('.','')
            email='@'.join(email)
            ans.add(email)
        return len(ans)