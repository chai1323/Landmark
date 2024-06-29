# import sqlite3
 
# # Connecting to sqlite
# conn = sqlite3.connect('Hotel_Dtabase.db')
 
# # Creating a cursor object using the  
# # cursor() method
# cursor = conn.cursor()
# table="""
# Create table Hotel_service(Booking_id varchar(30),roomno VARCHAR(50),firstname varchar(30),
# lastname varchar(30), address varchar(50),pincode int,
# email varchar(50),
# phone int,
# checkin Date,
# checkout Date,
# days_between int,
# bedtype varchar(20),
# bedtype_price int,
# extend_price int,
# triptype varchar(20),
# check_in_time Time,
# check_out_time Time,
# extend_check_out Date,
# payment_status varchar(10));
 
# """
# hotel="""
# Create table Hotel_resources(wifi_password varchar(30),hotel_name VARCHAR(50),hotel_year varchar(30),
# hotel_address varchar(50),
# hotel_pincode int,
# hotel_email varchar(50),
# reception_number int,
# extra_bed int,
# water_bottle int,
# bedsheet int,
# pillow int);
 
# """

# extend="""
# Create table Extend(
# booking_id varchar(30),
# roomno varchar(50),
# checkin Date,
# check_in_time Time
# );
# """
# # Creating table
 
# cursor.execute(table)
 
# cursor.execute('''INSERT INTO Hotel_service
#                    VALUES ('EC-123451', '1', 'Chaitanya', 'Vargas', '855-2487 Neque Rd.', '2032', 'lacus.Cras.interdum@Duis.ca', '1-195-805-5145', '2024-05-13', '2024-05-17', NULL, 'Queen', '100', NULL, 'Business trip', '00:00:00', '06:00:00', NULL, 'Done')''')
 
# cursor.execute('''INSERT INTO Hotel_service
#                    VALUES ('EC-123452', '2', 'Odessa', 'Olsen', '928-9525 Amet Rd.', '9987', 'libero.Proin@congueelit.edu', '1-722-294-3023', '2024-05-15', '2024-05-20', NULL, 'Queen', '100', NULL, 'Leisure trip', '03:00:00', '00:00:00', NULL, 'Not Done')''')
 
# cursor.execute('''INSERT INTO Hotel_service
#                    VALUES ('EC-123453', '3', 'Hamdhan', 'Spence', 'Ap #457-5217 Sem. St.', '5332', 'Nullam.nisl@adipiscinglobortis.ca', '1-382-461-8630', '2024-05-14', '2024-05-19', NULL, 'Double', '300', NULL, 'Leisure trip', '21:00:00', '11:00:00', NULL, 'Done')''')
 
# cursor.execute('''INSERT INTO Hotel_service
#                    VALUES ('EC-123454', '4', 'Keith', 'Holt', '6978 Eu Ave', '6578', 'vel.convallis.in@litora.co.uk', '1-705-376-7389', '2024-05-21', '2024-05-23', NULL, 'King', '200', NULL, 'Business trip', '18:00:00', '16:00:00', NULL, 'Not Done')''')
 
# cursor.execute('''INSERT INTO Hotel_service
#                    VALUES ('EC-123455', '5', 'Tamekah', 'Johnston', 'P.O. Box 502, 5311 Dapibus Av.', '8722', 'Donec@ut.net', '1-222-206-6257', '2024-05-19', '2024-05-24', NULL, 'King', '200', NULL, 'Leisure trip', '15:30:00', '11:00:00', NULL, 'Done')''')
 
# cursor.execute('''INSERT INTO Hotel_service
#                    VALUES ('EC-123456', '6', 'Portia', 'Walls', '3242 Et Rd.', '44463', 'sagittis@magnaSedeu.net', '1-426-963-9901', '2024-05-19', '2024-05-26', NULL, 'Double', '300', NULL, 'Leisure trip', '16:00:00', '10:00:00', NULL, 'Done')''')
 
# cursor.execute('''INSERT INTO Hotel_service
#                    VALUES ('EC-123457', '7', 'Cherokee', 'Preston', 'Ap #684-2829 Erat St.', '1732', 'enim.Sed@leoCrasvehicula.org', '1-579-656-8868', '2024-05-10', '2024-05-28', NULL, 'Queen', '100', NULL, 'Business trip', '07:00:00', '12:00:00', NULL, 'Not Done')''')
 
# cursor.execute('''INSERT INTO Hotel_service
#                    VALUES ('EC-123458', '8', 'Wylie', 'Foley', '9865 Dictum. Avenue', '363712', 'est.Nunc@egestas.ca', '1-705-328-1674', '2024-05-18', '2024-05-20', NULL, 'Queen', '100', NULL, 'Business trip', '03:00:00', '18:00:00', NULL, 'Done')''')
 
# cursor.execute('''INSERT INTO Hotel_service
#                    VALUES ('EC-123459', '9', 'Nichole', 'Carey', 'P.O. Box 524, 3928 Et Rd.', '63247', 'tincidunt.nibh.Phasellus@amagnaLorem.edu', '1-835-878-2075', '2024-05-20', '2024-05-30', NULL, 'Double', '300', NULL, 'Business trip', '09:00:00', '12:00:00', NULL, 'Not Done')''')
 
# cursor.execute('''INSERT INTO Hotel_service
#                    VALUES ('EC-1234510', '10', 'Cheryl', 'Cox', '412-5150 Gravida. Rd.', '35318', 'amet.consectetuer@volutpat.co.uk', '1-677-273-5522', '2024-05-24', '2024-05-28', NULL, 'King', '200', NULL, 'Leisure trip', '14:00:00', '22:00:00', NULL, 'Done')''')
 
# cursor.execute(hotel)

# cursor.execute('''INSERT INTO Hotel_resources
#                VALUES ('landwifi123','LANDMARK','2010','123,xyz','456456','landmark@gmail.com','9876543210','10','30','10','10')''')


# cursor.execute(extend)

# cursor.execute('''INSERT INTO Extend VALUES('EC-1234511','4','2024-05-23','18:00:00')''')
# # Display data inserted S
# print("Data Inserted in the table: ")
# data=cursor.execute('''SELECT * FROM Hotel_service''')
# for row in data:
#     print(row)

# dat=cursor.execute('''SELECT * FROM Hotel_resources''')
# for row in dat:
#     print(row) 
# ext=cursor.execute('''SELECT * FROM Extend''')
# for row in ext:
#     print(row)
# # Commit your changes in the database    

# conn.commit()
 
# # Closing the connection
# conn.close()




import sqlite3
 
# Connecting to sqlite
conn = sqlite3.connect('Hotel_Dtabase.db')
 
# Creating a cursor object using the  
# cursor() method
cursor = conn.cursor()
table="""
Create table Hotel_service(Booking_id varchar(30),roomno VARCHAR(50),firstname varchar(30),
lastname varchar(30), address varchar(50),pincode int,
email varchar(50),
phone int,
checkin Date,
checkout Date,
days_between int,
bedtype varchar(20),
bedtype_price int,
extend_price int,
triptype varchar(20),
check_in_time Time,
check_out_time Time,
extend_check_out Date,
payment_status varchar(10));
 
"""
hotel="""
Create table Hotel_resources(wifi_password varchar(30),hotel_name VARCHAR(50),hotel_year varchar(30),
hotel_address varchar(50),
hotel_pincode int,
hotel_email varchar(50),
reception_number int,
extra_bed int,
water_bottle int,
bedsheet int,
pillow int);
 
"""

extend="""
Create table Extend(
booking_id varchar(30),
roomno varchar(50),
new_checkin Date,
check_in_time Time
);
"""
# Creating table
 
cursor.execute(table)
 
cursor.execute('''INSERT INTO Hotel_service
                   VALUES ('EC-123451', '1', 'Chaitanya', 'Vargas', '855-2487 Neque Rd.', '2032', 'lacus.Cras.interdum@Duis.ca', '1-195-805-5145', '2024-05-13', '2024-05-17', NULL, 'Queen', '100', NULL, 'Business trip', '00:00:00', '06:00:00', NULL, 'Done')''')
 
cursor.execute('''INSERT INTO Hotel_service
                   VALUES ('EC-123452', '2', 'Odessa', 'Olsen', '928-9525 Amet Rd.', '9987', 'libero.Proin@congueelit.edu', '1-722-294-3023', '2024-05-15', '2024-05-20', NULL, 'Queen', '100', NULL, 'Leisure trip', '03:00:00', '00:00:00', NULL, 'Not Done')''')
 
cursor.execute('''INSERT INTO Hotel_service
                   VALUES ('EC-123453', '3', 'Hamdhan', 'Spence', 'Ap #457-5217 Sem. St.', '5332', 'Nullam.nisl@adipiscinglobortis.ca', '1-382-461-8630', '2024-05-14', '2024-05-19', NULL, 'Double', '300', NULL, 'Leisure trip', '21:00:00', '11:00:00', NULL, 'Done')''')
 
cursor.execute('''INSERT INTO Hotel_service
                   VALUES ('EC-123454', '4', 'Keith', 'Holt', '6978 Eu Ave', '6578', 'vel.convallis.in@litora.co.uk', '1-705-376-7389', '2024-05-21', '2024-05-23', NULL, 'King', '200', NULL, 'Business trip', '18:00:00', '16:00:00', NULL, 'Not Done')''')
 
cursor.execute('''INSERT INTO Hotel_service
                   VALUES ('EC-123455', '5', 'Tamekah', 'Johnston', 'P.O. Box 502, 5311 Dapibus Av.', '8722', 'Donec@ut.net', '1-222-206-6257', '2024-05-19', '2024-05-24', NULL, 'King', '200', NULL, 'Leisure trip', '15:30:00', '11:00:00', NULL, 'Done')''')
 
cursor.execute('''INSERT INTO Hotel_service
                   VALUES ('EC-123456', '6', 'Portia', 'Walls', '3242 Et Rd.', '44463', 'sagittis@magnaSedeu.net', '1-426-963-9901', '2024-05-19', '2024-05-26', NULL, 'Double', '300', NULL, 'Leisure trip', '16:00:00', '10:00:00', NULL, 'Done')''')
 
cursor.execute('''INSERT INTO Hotel_service
                   VALUES ('EC-123457', '7', 'Cherokee', 'Preston', 'Ap #684-2829 Erat St.', '1732', 'enim.Sed@leoCrasvehicula.org', '1-579-656-8868', '2024-05-10', '2024-05-28', NULL, 'Queen', '100', NULL, 'Business trip', '07:00:00', '12:00:00', NULL, 'Not Done')''')
 
cursor.execute('''INSERT INTO Hotel_service
                   VALUES ('EC-123458', '8', 'Wylie', 'Foley', '9865 Dictum. Avenue', '363712', 'est.Nunc@egestas.ca', '1-705-328-1674', '2024-05-18', '2024-05-20', NULL, 'Queen', '100', NULL, 'Business trip', '03:00:00', '18:00:00', NULL, 'Done')''')
 
cursor.execute('''INSERT INTO Hotel_service
                   VALUES ('EC-123459', '9', 'Nichole', 'Carey', 'P.O. Box 524, 3928 Et Rd.', '63247', 'tincidunt.nibh.Phasellus@amagnaLorem.edu', '1-835-878-2075', '2024-05-20', '2024-05-30', NULL, 'Double', '300', NULL, 'Business trip', '09:00:00', '12:00:00', NULL, 'Not Done')''')
 
cursor.execute('''INSERT INTO Hotel_service
                   VALUES ('EC-1234510', '10', 'Cheryl', 'Cox', '412-5150 Gravida. Rd.', '35318', 'amet.consectetuer@volutpat.co.uk', '1-677-273-5522', '2024-05-24', '2024-05-28', NULL, 'King', '200', NULL, 'Leisure trip', '14:00:00', '22:00:00', NULL, 'Done')''')
 
cursor.execute(hotel)

cursor.execute('''INSERT INTO Hotel_resources
               VALUES ('landwifi123','LANDMARK','2010','123,xyz','456456','landmark@gmail.com','9876543210','10','30','10','10')''')


cursor.execute(extend)

cursor.execute('''INSERT INTO Extend VALUES('EC-1234511','4','2024-05-23','18:00:00')''')
# Display data inserted S
print("Data Inserted in the table: ")
data=cursor.execute('''SELECT * FROM Hotel_service''')
for row in data:
    print(row)

dat=cursor.execute('''SELECT * FROM Hotel_resources''')
for row in dat:
    print(row) 
ext=cursor.execute('''SELECT * FROM Extend''')
for row in ext:
    print(row)
# Commit your changes in the database 

create_table_query = '''
CREATE TABLE IF NOT EXISTS user_history (
    booking_id TEXT PRIMARY KEY,
    message TEXT DEFAULT ''
);
'''

cursor.execute(create_table_query)

# SQL command to insert booking IDs into the user_history table
insert_data_query = '''
INSERT INTO user_history (booking_id, message) VALUES (?,?);
'''

# List of booking IDs to insert
booking_ids = [
    "EC-123451",
    "EC-123452",
    "EC-123453",
    "EC-123454",
    "EC-123455",
    "EC-123456",
    "EC-123457",
    "EC-123458",
    "EC-123459",
    "EC-1234510"
]

# Iterate through the booking IDs and insert each one into the user_history table
for booking_id in booking_ids:
    cursor.execute(insert_data_query, (booking_id, ''))


conn.commit()
 
# Closing the connection
conn.close()