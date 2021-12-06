# iwocaPay fullstack task

Hey 👋 welcome to our fullstack task. Take a look around and familiarise yourself with the code base. The frontend code is in the [./frontend](./frontend) directory, it's React + TypeScript (built with create-react-app). The backend code is in the [./backend](./backend) directory, it's a django application. Each has a README to get you all set up.

There are currently two pages on the frontend:

- http://localhost:3000/pay/:sellerHandle
  - This is where sellers send their buyers to pay their invoices, the seller handle is designed to be human readable and map to a single seller.
- http://localhost:3000/seller/:sellerId
  - This is where sellers can go to update their unique handle.

There are three endpoints on the backend:

- GET http://localhost:8000/api/sellers/:sellerId
  - Returns seller data using their unique id.
- GET http://localhost:8000/api/sellers/handle/:sellerHandle
  - Returns seller data user their unique handle.
- PUT http://localhost:8000/api/sellers/:sellerId
  - Updates the handle of a seller.

You can drop into the django admin (after creating a superuser) and add a new seller to test with: http://localhost:8000/admin/

## The task

There are two features we'd like you to implement, it should take up to 3 hours altogether.

1. At the moment sellers are unable to change their unique handle. They should be able to go to their seller page on the frontend (http://localhost:3000/seller/:sellerId) and update it there but it hasn't been implemented yet.

2. There's a risk that sellers may update their seller handles after already sharing their pay links with their customers, therefore breaking them. It should be possible for sellers to change their seller handles but not break existing links that used their old handles. For example, if a seller has the handle `acme` their customers would be able to go to `/pay/acme` to pay their invoices. However that link should continue to work when the seller changes their handle to `acme-inc`.
