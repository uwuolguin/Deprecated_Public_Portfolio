import tableauserverclient as TSC

tableau_auth = TSC.PersonalAccessTokenAuth('uwu96', 'Z7ip8aXtTkOOsW1x6hK3VQ==:pDzK0qHrO4m7PfJ36C7olcvJoYjIOhP0', 'bulls')
server = TSC.Server('https://10ax.online.tableau.com/', use_server_version=True)
server.auth.sign_in(tableau_auth)

with server.auth.sign_in(tableau_auth):
    all_workbooks_items, pagination_item = server.workbooks.get()
    print([(workbook.name,workbook.id) for workbook in all_workbooks_items])
    