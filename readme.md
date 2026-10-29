# Insight

Personal Financial Analysis Agent.  Parse & Analyze series of financial reports to help me see what I don't see.  This is to aid me quickly grasp how the company is doing over time.

## Scenario Usage

See phases for more detail.

1. User upload financial repfort
2. Programe creates a company profile or folder for it.
3. Start parsing PDF or xls file
4. Feed parse data to LLM for response 

## Most Current Scope 

Detail list of items to work on: Development Flow > Phase 1
- [ ] Manually create xls file
- [ ] RAW data into Pandas `DataFlow`
- [ ] Extract revene, capital, assets, debt...etc.
    -[ ] Turn each into mathmatical functions



---
**What I need to do next**

- [ ] Copy LLM translated financial statement into xls file.
- [ ] Put it in Pandas
- [ ] Create DataFrame $\rightarrow$ `.head()`, `info()`, `tail()`
    - Learn more functions along the way.

- [ ] Follow `README` guide lines for RDD.

---

# Development Flow
[ Data Source ] $\rightarrow$ [ Python Backend ] $\rightarrow$ [ API ] $\rightarrow$ [ React ]

## 🧩 Components:

*Item 1.* **The Logic (Panda):** Use Pandas to calculate the porfolio ROI, Variance, and Spend.

*Item 2.* **Thge Bridge (FastAPI/FLask):** Create API endpoint (e.g., `/api/fiance/summary`). Takes Pandas DataFrame and converts it to JSON.

*Item 3.* **The Display (Angular/TypeScript):**
- Angular calls the API using HttpClient.
- TypeScript defines an `Interface` to handle the financial data.
- **React Components** (like HTML tables or Charts) display the numbers beautifull on a dashboard.

*Item 4.* **The Export (openpyxl):** For users to "Export."  Backend triggers openpyxl to create formatted spreadsheet.

## Phases
$\rightarrow$ Claude: Building a financial analysis app with local LLM

1. **Data Wangling Foundation:** Read spreadsheet, compute ratios
- raw data layuer everthing later gets built on - you need clean numbers before an LLM can reason about them.
- [ ] Take compan's income statement / balancesheet.
- [ ] Load into Pandas, pull revenue, net income...etc.

2. **Document Parsing:** Extract text/tables from real PDF
- Real filing arrives in PDFs, not clean spreadsheets.  This is the parser your app will actually need to *automate things*.
- [ ] Use `pdfplumber` to pull out management discussion section and financial statement tables.
- [ ] Save the result in structured text/dict.

3. **Talk to LLM:** Sumjmarize a filing in plain English
- 1st reals use of LLM in pipeline - validates that the model can actually do the analysis task before you add complexity.
- [ ] Send text from phase 2 to a hosted LLM API.
- [ ] Prompt it to summarize the filing's key risks and performance in 5 bullet points.
- [ ] Iterate on your prompt until the output is consistently useful.

4. **Structured Extraction:** Force the LLM to output clean JSON
- Turns 'the LLM said something' into 'the app has typed data it can chart, store, and compare across companies'.
- [ ] Define a **Pydantic model** (Revenue, NetIncome, KeyRisks, Sentiment.)
- [ ] Prompt the LLM to return exactly that JSON shape instead of prose.
- [ ] Validate the response and reject / retry on malformed output.

5. **Go Local:** Swap the hosted API for local Ollama...
- This is where you test your local model is good enough for your accuracy bar... Before you build your whole app around it.
- [ ] Run local LLM, re-run phase 4 extraction against it and compare accuracy.

6. **RAG - Q&A Over a Report:** Aks question across a whole filing
- Filing is too long to paste in whole - retrieval is how you answer specific questions without blowing the context window.
- [ ] Chunk the full 10-K text, embed the chunck into a vector DB
    - [ ] Build loop: user ask 'what changed in gross margin YoY?'
        - Retrieve the relevant chuncks, and feed only those to the LLM to answer.

7. **Tools _ Agent Loop:** Let the model decide what to do...
- This is actual *agent*  step - multi-step reasoning and tool use instead of one prompt in, one answer out.
- [ ] Give LLM callable tools: `calculate_ratio()`, `search_filing()`, `get_stock_price()`.
- [ ] Wrap it in PydanticAI or LangGraph so it decides, pre question, whether to comput, retrieve, or just answer - looping until it has enough respond.
- [ ] Look into error handling... so it agent doesn't go into infininte loop.

