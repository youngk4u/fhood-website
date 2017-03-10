import braintree

braintree.Configuration.configure(braintree.Environment.Sandbox,
                                  merchant_id="mdq7s89q3b92n4m8",
                                  public_key="2ky4vj9s74djdnfs",
                                  private_key="use_your_private_key")
                                  
@app.route("/client_token", methods=["GET"])
def client_token():
  return braintree.ClientToken.generate()
  
  
@app.route("/checkout", methods=["POST"])
def create_purchase():
  nonce_from_the_client = request.form["payment_method_nonce"]
  # Use payment method nonce here...
  
  
result = braintree.Transaction.sale({
    "amount": "10.00",
    "payment_method_nonce": nonce_from_the_client,
    "options": {
      "submit_for_settlement": True
    }
})
