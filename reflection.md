# Reflection Questions

1. Which issues were the easiest to fix, and which were the hardest? Why?
->Easiest: Fixing mutable default arguments, unused imports, and adding docstrings were straightforward.  
->Hardest: Refactoring the global variable usage and removing `eval()` safely were harder, as they required deeper understanding of program flow and security implications.

---

2. Did the static analysis tools report any false positives?
No major false positives were found.  
Flake8 flagged minor formatting issues (like line length) that didn’t affect functionality, but they helped maintain consistent style.

---

3. How would you integrate static analysis tools into your workflow?
Static analysis tools should be part of every **development and CI/CD pipeline**.  
I would configure **GitHub Actions** to automatically run **Pylint**, **Flake8**, and **Bandit** on every commit or pull request, preventing insecure or low-quality code from being merged.

---

4️. What tangible improvements did you observe after applying the fixes?
- Code readability and maintainability improved significantly.  
- Security risks (like `eval`) were removed.  
- File handling is now safer and cross-platform compatible (with explicit UTF-8 encoding).  
- Overall code quality increased — confirmed by a **Pylint score of 9.81/10** and **zero Bandit issues**.

---

# Summary

| **Tool** | **Result Summary** |
|-----------|--------------------|
| **Pylint** |  Final score: **9.81/10** — only minor “global statement” warning remaining |
| **Flake8** |  No PEP8 or style violations detected |
| **Bandit** |  No security vulnerabilities identified |
| **Execution Test** |  Program runs successfully with correct outputs |

---

# Conclusion
Static code analysis improved my program’s **security, readability, and structure**.  
These tools helped me adopt better coding habits and write more reliable software by identifying issues that are often missed during normal testing.

---
