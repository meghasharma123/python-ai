import streamlit as st

def safe_margin(revenue, expense):
    try:
        return (revenue -expense) * 100 / revenue
    except ZeroDivisionError:
        return "Revenue 0 can't be process"
    except TypeError:
        return "Args type is not valid"
    except:
        return "Unable to process at this moment. Try again later!"

# print(safe_margin(15, 5))
# print(safe_margin(0, 10))
# print(safe_margin("erer", 10))

# Exercise

def safe_chai_bill(cups, price_per_cup):
    try:
        cups = int(cups)
        price_per_cup = float(price_per_cup)

        if(cups < 1):
            return "Cups must be atleast 1."

        return cups * price_per_cup, None
    
    except ValueError:
        return "Please enter numbers only"

# print(safe_chai_bill("3", "15"))  
# print(safe_chai_bill(2, 15))        
# print(safe_chai_bill("two", 15))    
# print(safe_chai_bill(0, 15)) 

st.set_page_config(
    page_title="Chai Bill Calculator",
    page_icon="☕",
    layout="centered"
)

st.title("☕ Chai Bill Calculator")
st.caption("Calculate your chai bill instantly!")

st.divider()

cups = st.number_input(
    "Number of cups",
    min_value=0,
    step=1,
    value=1
)

price = st.number_input(
    "Price per cup (₹)",
    min_value=0.0,
    step=5.0,
    value=10.0
)

if st.button("Calculate Bill", use_container_width=True):

    total, error = safe_chai_bill(cups, price)

    if error:
        st.error(error)
    else:
        st.success("Bill calculated successfully!")
        st.metric(
            label="Total Chai Bill",
            value=f"₹{total:.2f}"
        )

# to run streamlit -> `streamlit run error_handling`