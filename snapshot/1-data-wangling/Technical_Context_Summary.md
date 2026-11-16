# Project Context: Financial Analysis Agent (Data Pipeline)

### 1. Current Objective
Building a production-grade data extraction pipeline for financial statements using Python and Pandas. The goal is to transition from basic script-writing to professional, defensive engineering that handles "dirty" financial data.

### 2. Core Architecture Implemented
*   **Lookup Logic:** Transitioned from slow Python `for` loops to **Pandas Index Intersection** (`df.index.intersection(aliases)`) for $O(1)$ label lookups.
*   **The "Clean-at-the-Gate" Pattern:** Implemented a post-load sanitization pipeline. Data is cleaned immediately after loading to avoid redundant string operations during extraction.
*   **Defensive Extraction:** Moved from returning sentinel values (like `0.0`) to using **`None`** and **`np.nan`** to distinguish between "Label Not Found," "Value is Zero," and "Data is Missing."
*   **Sanitization Pipeline:** Created a robust `parse_magnitude` helper function used via `.apply()` to handle:
    *   **Currency/Symbols:** Stripping `$`, commas, and whitespace.
    *   **Accounting Negatives:** Converting parentheses `(100)` to negative floats `-100.0`.
    *   **Magnitude Suffixes:** Converting `K` (1e3), `M` (1e6), and `B` (1e9) into their full numeric values.
    *   **Stability:** Replaced fragile `float()` casts with **`pd.to_numeric(errors='coerce')`** to prevent crashes on non-numeric strings (e.g., "N/A", "TBD").

### 3. Technical Standards Established
*   **Memory Management:** Using **`.copy()`** when modifying DataFrames to avoid `SettingWithCopyWarning` and preserve the raw "Audit Trail" data.
*   **Complexity Trade-offs:** Opted for `.apply()` over vectorization for magnitude logic to prioritize **readability and maintainability** given the small scale of financial statements (hundreds vs. millions of rows).
*   **Development Workflow:** Adopting the **"Atomic Iteration"** method: solving for a single scalar $\rightarrow$ handling edge cases $\rightarrow$ integrating into Pandas $\rightarrow$ wrapping in defensive production code.

### 4. Pending Roadmap (The "Next Layer")
*   **Aggregation & Analytics:** Implementing vectorized calculations for financial metrics (e.g., Variance Analysis, YoY Growth, Expense Ratios).
*   **Schema Validation:** Adding a "Schema Check" layer to verify column existence and data types before the pipeline runs.
*   **Flexible Indexing:** Handling "Schema Drift" where column names change between different clients' files.

***

**CodeCoach Note:** I am ready for the new thread. When you start, just paste this and tell me: *"I'm ready to move to the Aggregation & Analytics layer,"* or let me know if you have a new specific problem to solve!