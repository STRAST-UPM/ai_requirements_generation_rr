# Model References

This table provides a description for each of the model references used in the results section.

| Model Reference   | Description                                     |
|:------------------|:------------------------------------------------|
| h                 | Human consensus                                 |
| l0                | LLaMa, optimal hyperparameters (1st execution)  |
| l0_ii             | LLaMa, optimal hyperparameters (2nd execution)  |
| l0_iii            | LLaMa, optimal hyperparameters (3rd execution)  |
| l0_iv             | LLaMa, optimal hyperparameters (4th execution)  |
| l0a               | LLaMa, prompt without repetitions               |
| l0b               | LLaMa, simplified prompt                        |
| l1                | LLaMa, lower temperature                        |
| l2                | LLaMa, higher temperature                       |
| l3                | LLaMa, merged 4 generations                     |
| l4                | LLaMa, no explicit chain-of-thought             |
| l5                | LLaMa, few-shot                                 |
| q0                | QWen, optimal hyperparameters                   |
| q0_ii             | QWen, optimal hyperparameters (2nd execution)   |
| q0_iii            | QWen, optimal hyperparameters (3rd execution)   |
| q0_iv             | QWen, optimal hyperparameters (4th execution)   |
| q1                | QWen, lower temperature                         |
| q2                | QWen, higher temperature                        |
| m0                | Mixtral, optimal hyperparameters                |
| m0_ii             | Mixtral, optimal hyperparameters (2nd execution)|
| m0_iii            | Mixtral, optimal hyperparameters (3rd execution)|
| m0_iv             | Mixtral, optimal hyperparameters (4th execution)|
| m1                | Mixtral, lower temperature                      |
| m2                | Mixtral, higher temperature                     |
| g0                | GPT-4, optimal hyperparameters                  |
| g0_ii             | GPT-4, optimal hyperparameters (2nd execution)  |
| g0_iii            | GPT-4, optimal hyperparameters (3rd execution)  |
| g0_iv             | GPT-4, optimal hyperparameters (4th execution)  |
| g1                | GPT-4, lower temperature                        |
| g2                | GPT-4, higher temperature                       |

For the details of each model generation, including the hyperparameters used, the model version, and the date of execution, please refer to the `execution_details.md` files in (`doc/` directory). Each model generation has its own execution details file, which provides a comprehensive overview of the execution parameters and results.

## Version History

| Version | Date       | Change                                            |
| ------- | ---------- | ------------------------------------------------- |
| 1.0     | 2025‑06-30 | Initial public release matching paper submission. |
| 2.0     | 2025‑12-01 | Second release including additional data files.   |

---

*Last updated : 2025‑12‑01*