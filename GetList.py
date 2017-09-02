from urllib.request import urlopen
def GetActiveUsers():
	ActiveUsers = urlopen("http://192.241.244.177/ChatApplication/ActiveUsers.php")
	# ActiveUsersData = ActiveUsers.decode()
	for Data in ActiveUsers:
		ActiveUsersData = Data.decode()
	for Name in str(ActiveUsersData).split(","):
		print(Name)
GetActiveUsers()