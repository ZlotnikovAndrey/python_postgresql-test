import psycopg2
from config import host, user, password, db_name

try:
    # connect to exist database
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True

    # the cursor for perfoming database operations
    # cursor = connection.cursor()

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )

        print(f"Server version: {cursor.fetchone()}")

    # create a new table
    with connection.cursor() as cursor:
        cursor.execute(

        """CREATE TABLE shell_and_bus(
           drawing varchar(50) NOT NULL unique ,
            type varchar(50) ,
            size varchar(50) ,
            diameter varchar(50) NOT NULL,
            PRIMARY KEY (drawing));"""

        """CREATE TABLE detail_size(
            drawing varchar(50) NOT NULL unique,
            size varchar(50) NOT NULL ,
            note varchar(50),
            PRIMARY KEY (drawing));"""

        """CREATE TABLE summary_list_C(
            name varchar(50) NOT NULL,
            drawing varchar(50) NOT NULL unique,
            material varchar(50) ,
            amount varchar(50) NOT NULL,
            PRIMARY KEY (drawing),
            FOREIGN KEY (drawing) REFERENCES shell_and_bus(drawing),
            FOREIGN KEY (drawing) REFERENCES detail_size(drawing));"""

        """INSERT INTO detail_size (drawing, size) VALUES
            ('8ТП.310.007','280х240х4'),('8ТП.310.008-048','1370х270х4'),('8ТП.310.008-050','1372х200х4'),
            ('8ТП.310.008-075','562х350х4'),('8ТП.310.017','380х380х4'),('8ТП.310.017-001','293х380х4'),('8ТП.310.006-009','250х180х4'),
            ('8ТП.154.044','980х120х6'),('8ТП.154.044-001','706х120х6'),('8ТП.154.355.001-005','280х50х4'),('8ТП.154.355.001-076','248х50х4'),
            ('8ТП.346.003-002','1428х300х6'),('8ТП.346.003-018','1004х300х6'),('8ТП.346.005-007','1835х172х6'),('8ТП.140.006','Плазма'),
            ('8ТП.150.012','Плазма'),('8ТП.557.047','240х150х4'),('8ТП.557.097-003','70х70х4'),('8ТП.154.001-018','624х12х4')
        ;"""

        """INSERT INTO shell_and_bus (drawing, type, size, diameter) VALUES
        ('8ТП.344.001-001', 'Прямая', '500', '678'), ('8ТП.344.001-002', 'с зиг', '501', '678'), (
        '8ТП.344.001-003', 'угл45', '502', '678'), ('8ТП.344.001-004', 'с зиг45', '503', '678'), (
        '8ТП.344.001-005', 'отпай', '504', '678'), ('8ТП.344.001-006', 'рыбка', '505', '678'), (
        '8ТП.344.001-007', 'Прямая', '506', '678'), ('8ТП.344.001-008', 'с зиг', '507', '678'), (
        '8ТП.344.001-009', 'угл46', '508', '678'), ('8ТП.344.001-010', 'с зиг46', '509', '678'), (
        '8ТП.344.001-011', 'отпай', '510', '412'), ('8ТП.344.001-012', 'рыбка', '511', '412')
        ;"""
            
        )

        connection.commit()
        print("[INFO] Table created successfully")

except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        # cursor.close()
        connection.close()
        print("[INFO] PostgreSQL connection closed")