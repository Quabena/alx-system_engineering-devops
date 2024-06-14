SHELL PERMISSIONS
0-iam_betty file switches the current user to the user betty
1-who_am_i file prints the effective username of the current user
2-groups - prints all the groups that the current user is part of
3-new_owner - changes the owner of the file hello to betty
4-empty - creates an empty file called hello
5-execute - adds execute permission to the owner of the file hello
6-multiples_permissions -  adds execute permission to the owner and the group owner, and read permission to other users, to the file hello
7-everybody - adds execution permission to the owner and the other users, to the file hello
8-James_bond - gives no permission to the owner and group, but all permissions to Other users
9-John_Doe - set the mode of the file hello to -rwxr-x-wx echo 9-John_Doe - set the mode of the file hello to -rwxr-x-wx
10-mirror_permissions - sets the mode of the hello same as olleh mode
11-directories_permissions - adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users
12-directory_permissions - creates a directory called my_dir with permissions 751 in the working directory
13-change_group - changes the group owner to school for the file hello
100-change_owner_and_group - changes the owner to vincent and the group owner to staff for all the files in the working directory
101-symbolic_link_permissions - changes the owner and the group owner of _hello to vincent and staff respectively
102-if_only - changes the owner of the file hello to betty only it is owned by the user guillaume
103-Star_Wars - Plays StarWars IV episode in the terminal
