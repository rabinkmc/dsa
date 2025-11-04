from typing import List


class Solution:

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        visited = set()
        graph = {}
        for account in accounts:
            name = account[0]
            emails = account[1:]
            for email in emails:
                if email not in graph:
                    graph[email] = set()
                for other_email in emails:
                    if other_email != email:
                        graph[email].add(other_email)

        def dfs(node, emails):
            visited.add(node)
            emails.append(node)
            for children in graph[node]:
                if children not in visited:
                    dfs(children, emails)

        result = []
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                emails = []
                if email not in visited:
                    dfs(email, emails)
                emails.sort()
                if emails:
                    result.append([name] + emails)
                visited.add(email)
        return result


accounts = [
    ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
    ["John", "johnsmith@mail.com", "john00@mail.com"],
    ["Mary", "mary@mail.com"],
    ["John", "johnnybravo@mail.com"],
]

Solution().accountsMerge(accounts)
