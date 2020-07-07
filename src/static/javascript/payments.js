function card(data) {
    document.addEventListener('DOMContentLoaded', (event) => {
        var stripe = Stripe(data.stripe_publishable_key);
        var elements = stripe.elements();

        var style = {
            base: {
                color: "#32325d",
                fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
                fontSmoothing: "antialiased",
                fontSize: "16px",
                "::placeholder": {
                    color: "#aab7c4"
                }
            },
            invalid: {
                color: "#fa755a",
                iconColor: "#fa755a"
            }
        };

        var card = elements.create("card", { style: style });
        card.mount("#card-element");
    });
}

/* return {
    stripe: stripe,
    card: card,
    clientSecret: data.clientSecret
}; */