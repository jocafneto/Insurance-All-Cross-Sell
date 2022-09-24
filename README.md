# Insurance-All-Cross-Sell
-  A **classification project** that uses ML Model to **learn to rank** their customers to sell a **company's new product**.

## **Company Name:**

-  **Insurance All Company**

## **What the Company do?**

-  Sell **health insurance** to its customers.

## **What's the business problem?**

-  The **company** is trying to know which are **the best customers** to **offer** its new product, **auto insurance**.

## **Which are the main strategy?**

-  The **company** will call initially **5.000 customers**, so we need to know which to call.

## **Types of data:**
 * **id**: Unique ID.
 * **gender**: Customer's gender.
 * **age**: Customer's age.
 * **region_code**: Unique code for the region of the customer.
 * **policy_sales_channel**: Anonymised Code for the channel of outreaching to the customer ie. Different Agents, Over Mail, Over Phone, In Person, etc.
 * **driving_license**: **0** = Customer does not have DL; **1** = Customer already has DL.
 * **vehicle_age**: Age of the Vehicle.
 * **vehicle_damage**:  **0** = Customer didn't get his/her vehicle damaged in the past; **1** = Customer got his/her vehicle damaged in the past.
 * **previously_insured**: **1** = Customer already has Vehicle Insurance; **0** = Customer doesn't have Vehicle Insurance.
 * **annual_premium**: The amount customer needs to pay as premium in the year.
 * **vintage**: Number of Days, Customer has been associated with the company.
 * **response**: **1** = Customer is interested; **0** = Customer is not interested.


## **What kind of question we need to answer?**

1.   Qual a **porcentagem de clientes**, interessados em adquirir o seguro de veículo, que o time de vendas conseguirá fazendo **5.000 ligações**? E qual **retorno financeiro**, se comparado ao **modelo randômico**, se cada seguro de veículo custar **1000 reais**?

2.   E se **aumentarmos** a quantidade de ligações para **10.000**?

3.   E se agora, **aumentarmos** para **20.000** ligações?
