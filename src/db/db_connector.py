import paramiko
import time
import pandas as pd

class DBConnector:
    def __init__(self):
        """ Connect to the database and ssh server """        
        self.ssh = self.connect()
        self.db = self.mysql()

    def connect(self):
        """ Connect to the ssh server """
        ssh_key_path = "src/db/academy"
        ssh_host = "34.74.224.225"
        ssh_user = "academy"
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        private_key = paramiko.RSAKey(filename=ssh_key_path)
        ssh.connect(ssh_host, username=ssh_user, pkey=private_key)
        ssh_shell = ssh.invoke_shell()
        time.sleep(1)
        return ssh_shell
    
    def mysql(self):
        """ Connect to the mysql server """
        prompt = self.ssh
        prompt.send("mysql -u admin -p'>j.\zt'\\''cR89'\\''if:D' -h 35.231.115.227 -D dbacademychi" + "\n")
        time.sleep(1)
        return prompt
    
    def query(self, query:str = "SHOW TABLES;") -> str:
        """ Send a query to the database

        :param query: SQL query, defaults to "SHOW TABLES;"
        :type query: str, optional
        :return: Output of the query
        :rtype: str
        """        
        self.db.send(query + "\n")
        time.sleep(1)
        output = self.db.recv(4096).decode()
        return output

    def insert(self, table: str, values: str) -> str:
        """_summary_

        :param table: Table of database to insert values
        :type table: str, optional
        :param values: Values to insert
        :type values: str, optional
        :return: return of the query
        :rtype: str
        """        
        query = "INSERT INTO " + table + " VALUES " + values + ";"
        return self.query(query)
    
    def select(self, table: str, columns: str = "*",
                condition: str = "") -> pd.DataFrame:
        """Select values from a table

        :param table: Table to be search
        :type table: str, optional
        :param columns: Columns to be search, defaults to "*"
        :type columns: str, optional
        :param condition: Conditions of the search, defaults to ""
        :type condition: str, optional
        :return: Dataframe with the results or empty list
        :rtype: pd.DataFrame
        """        
        query = "SELECT " + columns + " FROM " + table + " " + condition + ";"
        return_query = self.query(query)
        table_returned = return_query.split(query)[1]
        lines_returned = table_returned.split("\n")[1:]
        if len(lines_returned) == 1:
            return []
        else:
            colums_df = lines_returned[1].split("|")[1:-1]
            colums_df = [column.strip() for column in colums_df]
            lines_df = []
            for line in lines_returned[3:-4]:
                line = line.split("|")[1:-1]
                line = [column.strip() for column in line]
                lines_df.append(line)
            return pd.DataFrame(lines_df, columns=colums_df)
        
    def delete(self, table: str, condition: str) -> str:
        """Delete values from a table

        :param table: Table to be delete
        :type table: str, optional
        :param condition: Conditions of the delete
        :type condition: str, optional
        :return: return of the query
        :rtype: str
        """        
        query = "DELETE FROM " + table + " " + condition + ";"
        return self.query(query)
    
    def destroy(self):
        self.db.close()

if __name__ == "__main__":
    db = DBConnector()
    print(db.select("User"))
    table = "User (IdUser, UserName, BirthDate, CPF, RG, UserPassword)"
    value = "(100, 'teste', '1999-01-01', '12345678910', '123456789', '123456789')"
    print(db.insert(table = table, values = value))
    print(db.delete("User", "WHERE IdUser = 100"))
    db.destroy()
