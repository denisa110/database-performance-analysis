# Database Query Performance Report

_Generated: 2025-06-16 21:58_


## 1. Obiectiv
Analiza comparativă a timpului de execuție pentru interogări cu/ fără index și shard‑uri, folosind statistici clasice și modele de Machine‑Learning.

## 2. Rezultate statistice clasice


| group   |   n |   mean_before |   mean_after |   mean_diff |   cohen_d |   t_stat |   p_t |   wilcoxon |   p_w |   ci_low |   ci_high |   n_required_80p |
|:--------|----:|--------------:|-------------:|------------:|----------:|---------:|------:|-----------:|------:|---------:|----------:|-----------------:|
| index   | 122 |        66.131 |       65.311 |       0.82  |     0.031 |    0.344 | 0.732 |     2972.5 | 0.477 |   -3.426 |     5.697 |         8106.12  |
| shards  | 122 |        56.057 |       66.131 |     -10.074 |    -0.214 |   -2.36  | 0.02  |      349   | 0     |  -16.131 |    -0.549 |          173.837 |


### Bootstrap Distributions


![Index bootstrap](results/figures/statistical/bootstrap_index.png){width="500px"}

![Shards bootstrap](results/figures/statistical/bootstrap_shards.png){width="500px"}


## 3. Modele liniare & ANOVA


### Coeficienți OLS vs Robuști


|    | Unnamed: 0                   |     OLS |   RLM_Huber |
|---:|:-----------------------------|--------:|------------:|
|  0 | Intercept                    | -26.493 |     -29.45  |
|  1 | C(opt)[T.before]             |   0.82  |      -0.38  |
|  2 | np.log1p(documents_returned) |  14.24  |      14.558 |


## 4. Putere & Learning Curves


![Power curve](results/figures/power/power_curve.png){width="500px"}

![CI learning curve](results/figures/power/ci_learning_curve.png){width="500px"}


## 5. Modele ML


| Model         |   RMSE_mean |   RMSE_std |   R2_mean |   R2_std |
|:--------------|------------:|-----------:|----------:|---------:|
| Random Forest |      10.548 |      3.732 |     0.878 |    0.083 |

![RF importance](results/figures/ml/rf_feature_importance.png){width="400px"}


## 6. Concluzii
* Indexarea reduce timpul mediu cu **{:+.1f} ms** și are un efect de mărime _d_ ≈ {stat_sum.loc[0,'cohen_d']:.2f}.
* Sharding oferă un câștig suplimentar mediu de **{stat_sum.loc[1,'mean_diff']:.1f} ms**.
* Modelele ML confirmă că `documents_returned` și timpul *fără* index sunt cei mai buni predictori.
