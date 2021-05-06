from smb.SMBConnection import SMBConnection

class ConnectToTheNetwork:

    def __init__(self, user_id, password, client_machine_name, server_name, server_ip, path, share_folder):
        self.user_id = user_id
        self.password = password
        self.client_machine_name = client_machine_name
        self.server_name = server_name
        self.server_ip = server_ip
        self.path = path
        self.share_folder = share_folder
        self.connection = self.connect()

    def connect(self):
        conn = SMBConnection(self.user_id, self.password, self.server_ip, self.server_name, use_ntlm_v2=True)
        conn.connect(self.server_ip, 139)
        return conn

    def copy_file(self, name, path_to_file, path_to_save):
        if name != '' and path_to_save != '':
            with open(path_to_save + '//' + name, 'wb') as fp:
                self.connection.retrieveFile(self.path, self.share_folder + '/' + path_to_file + '/' + name, fp)

    def copy_files(self, names, path_to_files, path_to_save):
        for name in names:
            self.copy_file(name, path_to_files, path_to_save)

    def count_files(self, mask, path):
        if mask is not None:
            shares = self.connection.listPath(self.path, self.share_folder + '/' + path)
            filtered_files = filter_files(shares, mask)
            return len(filtered_files)
        return 0