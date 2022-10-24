import car

monica = car.Car("chevrolet", "impala", "2016")
print(monica.get_descriptive_name(), monica.read_odometer())

tesla = car.ElectricCar("tesla", "model-Y", "2019")
print(tesla.get_descriptive_name(), tesla.fill_gas_tank())
