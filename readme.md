# Insight

- [ ] Project Goal
- [ ] Project Steps



# Project Requirements base Questions

## Finance KPI
- [ ] Is there a need?
    - List of financial KPI: For the Agent to ask in dquence?

## Development Blue Print
[ Data Source ] $\rightarrow$ [ Python B ackend ] $\rightarrow$ [ API ] $\rightarrow$ [ Angular Frontend ]

### Step-by-Step Flow:

*Item 1.* **The Logic (Panda):** Use Pandas to calculate the porfolio ROI, Variance, and Spend.

*Item 2.* **Thge Bridge (FastAPI/FLask):** Create API endpoint (e.g., `/api/fiance/summary`). Takes Pandas DataFrame and converts it to JSON.

*Item 3.* **The Display (Angular/TypeScript):**
- Angular calls the API using HttpClient.
- TypeScript defines an `Interface` to handle the financial data.
- **React Components** (like HTML tables or Charts) display the numbers beautifull on a dashboard.

*Item 4.* **The Export (openpyxl):** For users to "Export."  Backend triggers openpyxl to create formatted spreadsheet.


## Get working
There are 2 things that will have to happen.

- [ ] Learn React from tutorial

### Learn React for the presentation
Progress log


### Panda through AI
Progress log
- Just getting started with converting dictionary data to....a table?


## Question Arise along the way

- *Item 3* Display
    - [ ] Python has Numpy or Matplotlib.... What is this and how does it fit into my project