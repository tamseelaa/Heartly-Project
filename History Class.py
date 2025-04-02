Class History():
    def __init__(self):
        self.latest_max_rows=max_rows[]
        self.measurement_no=measurement_no[]
        
        
    def measurements(self,latest_max_rows):
        sql=f"select measurement from history order by desc() limit 8 "
        return self.max_row[:8]
        
    def measurement_data(self,measurement_no):
        sql_measurement= f"select * from history where latest_max_row.measurement_no= {self.measurement_no} "
        return self.measurement_no
        