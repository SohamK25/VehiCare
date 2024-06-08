## VehiCare is a smart solution designed to make managing vehicle servicing easy and efficient. 
---
### VehiCare is an online system designed to streamline the maintenance process for vehicle owners and service providers. Through a user-friendly interface, users can schedule service appointments, track vehicle service history, and communicate with service centres. Mechanics can easily manage their tasks, update vehicle status, and manage their own profile. Administrator can efficiently manage appointments, track service requests, and maintain customer, mechanic records. 
---
## FUNCTIONALITIES
### Customer
- customer will signup and login into system
- customer can make request for service of their vehicle by providing details (vehicle number, model, problem description etc.)
- After Request approved by admin, customer can check cost, status of service
- customer can delete request 
- customer can check status of Request - customer can check invoice details or repaired vehicles
- customer can send feedback to admin
- customer can see/edit their profile
---
### Mechanic
- mechanic will apply for job by providing details like (skills, address, mobile etc.)
- Admin will hire(approve) mechanic account based on skill
- After account approval, mechanic can login into system
- mechanic can see how many work (vehicles to repair) is assigned to me
- mechanic can change status of service ('Repairing', 'Repairing Done') according to work progress
- mechanic can see salary and how many vehicles he/she have repaired so far
- mechanic can send feedback to admin
- mechanic can see/edit their profile
---
### Admin
- First admin will login ( for username/password run following command in cmd )
```
py manage.py createsuperuser
```
- Give username, email, password and your admin account will be created.
- After login , admin can see how many customer, mechanic, recent service orders on dashboard
- Admin can see/add/update/delete customers
- Admin can see each customer invoice (if two request made by same customer it will show total sum of both request)
- Admin can see/add/update/delete mechanics
- Admin can approve(hire) mechanics (requested by mechanic) based on their skills
- Admin can see/update mechanic salary
- Admin can see/update/delete request/enquiry for service sent by customer
- Admin can also make request for service
- Admin can approve request for service made by customer and assign to mechanic for repairing and will provide cost according to problem description
- Admin can see all service cost of request (both approved and pending)
- Admin can see feedbacks sent by customer/mechanic
---
## HOW TO RUN THIS PROJECT
- Install Python(3.7.6) (Dont Forget to Tick Add to Path while installing Python)
- Open Terminal and Execute Following Commands :
```
pip install django==3.0.5
pip install django-widget-tweaks

```
- Download This Project Zip Folder and Extract it
- Move to project folder in Terminal. Then run following Commands :
```
py manage.py makemigrations
py manage.py migrate
py manage.py runserver
```
- Now enter following URL in Your Browser Installed On Your Pc
```
http://127.0.0.1:8000/
```
---
## Project Limitations
- Project require internet connectivity to work
- Certain features may not work on all types of browsers
- Some security concerns may present
- there may be instances of data discrepancies or inaccuracies
---
## Future Enhancements
- System can be converted to mobile applications
- Enhanced notifications and Predictive Maintainance Alerts
- Enhanced commmunication features
- Features to engage customer loyalty
- Expand service offerings
---
# Screenshots
- Home Page
![Screenshot 2024-04-22 062650](https://github.com/SohamK25/VehiCare/assets/149497770/9c6a219f-d4a8-4a54-af5e-2e468d3bb604) 

- Customer Sign In
![Screenshot 2024-04-22 062904](https://github.com/SohamK25/VehiCare/assets/149497770/d99f3c5c-a04c-44aa-bcae-e72e2186f19c)

- Mechanic Sign In
![Screenshot 2024-04-22 062952](https://github.com/SohamK25/VehiCare/assets/149497770/3b532ecd-8d0b-41d5-b862-0833a4583f35)

- Admin Login
![Screenshot 2024-04-22 071158](https://github.com/SohamK25/VehiCare/assets/149497770/6d9a7122-f8e9-47f5-8c68-0a78c68bdcda)

- Service Request
![Screenshot 2024-04-22 063735](https://github.com/SohamK25/VehiCare/assets/149497770/f3da1887-6ad0-4eca-ada1-130df746244d)


