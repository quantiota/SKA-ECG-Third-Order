# SKA-ECG Third Order

**Third-order SKA learning of the heartbeat: the learner reads the second-order result, one
step per cycle.**

## From the second order to the third

The second-order SKA learner gives one point per cycle in its cube (z₂, ż₂, P₂).

1. **Point** — u_k = (z₂, ż₂, P₂) of cycle k.
2. **Segment** — s_k = u_k − u_k−1, from one point to the next: the direction of the run.
3. **Direction** — c₃_k = cos(s_k, s_k−1), two successive segments compared: +1 the run goes on,
   −1 it turns back.
4. **Input** — v₃_k = (P₂_k − P₂_k−1) / P₂_k−1 · c₃_k, the simple return of P₂ (no log) times the direction, what the
   third-order learner reads, one step per cycle.

## The third-order axes

| | second order: one step per cycle | third order: one step per cycle |
|---|---|---|
| knowledge | z₂ = ‖Z₂‖, learned from the returns of c_k | z₃ = ‖Z₃‖, learned from v₃ = (P₂_k − P₂_k−1)/P₂_k−1 · c₃ |
| time step | Δt₂ = time between two cycles | Δt₃ = time between two cycles |
| rate | ż₂ = dz₂/dt₂ | ż₃ = dz₃/dt₃ |
| probability | P₂ = exp(−\|ΔH₂/H₂\|) | P₃ = exp(−\|ΔH₃/H₃\|) |

## Data

- [`aging/`](aging/) — PhysioNet Autonomic Aging, second order from
  [SKA-ECG-Second-Order](https://github.com/quantiota/SKA-ECG-Second-Order).
- [`ptb/`](ptb/) — PhysioNet PTB, lead II, second order from
  [SKA-ECG-Second-Order](https://github.com/quantiota/SKA-ECG-Second-Order).

Each holds `data/`, `figures/` and `vr/`, at three third-order scales: **2** (default, the cubes
linked below), 10 and 25. The scale is the last number of each file name, e.g.
`ska3_ecg_0060_scale25_scale25_scale2_vr.html` (first, second, third-order scale); a cube at another
scale has the same name with `_scale10` or `_scale25` at the end.

## Cubes — Autonomic Aging

One cube per woman: third-order learning (scale 2) of her second-order run (scale 25), first order at her selected scale.
Axes z₃, ż₃ and P₃ or Δt₃ (time between two cycles); colour = the sign of v₃ = (P₂_k − P₂_k−1)/P₂_k−1 · c₃. Open in a browser; a headset can enter VR.

| age | record | first-order scale | P₃ cube | Δt₃ cube |
|---|---|---|---|---|
| 20–24 | 0002 | 60 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0002_scale60_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0002_scale60_scale25_scale2_dt_vr.html) |
| 18–19 | 0044 | 25 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0044_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0044_scale25_scale25_scale2_dt_vr.html) |
| 60–64 | 0053 | 25 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0053_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0053_scale25_scale25_scale2_dt_vr.html) |
| 18–19 | 0060 | 25 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0060_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0060_scale25_scale25_scale2_dt_vr.html) |
| 55–59 | 0082 | 25 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0082_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0082_scale25_scale25_scale2_dt_vr.html) |
| 18–19 | 0098 | 25 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0098_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0098_scale25_scale25_scale2_dt_vr.html) |
| 45–49 | 0114 | 25 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0114_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0114_scale25_scale25_scale2_dt_vr.html) |
| 75–79 | 0153 | 25 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0153_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0153_scale25_scale25_scale2_dt_vr.html) |
| 25–29 | 0155 | 25 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0155_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0155_scale25_scale25_scale2_dt_vr.html) |
| 40–44 | 0164 | 40 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0164_scale40_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0164_scale40_scale25_scale2_dt_vr.html) |
| 85–92 | 0188 | 30 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0188_scale30_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0188_scale30_scale25_scale2_dt_vr.html) |
| 65–69 | 0214 | 25 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0214_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0214_scale25_scale25_scale2_dt_vr.html) |
| 70–74 | 0229 | 5 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0229_scale5_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0229_scale5_scale25_scale2_dt_vr.html) |
| 70–74 | 0237 | 25 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0237_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0237_scale25_scale25_scale2_dt_vr.html) |
| 18–19 | 0239 | 25 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0239_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0239_scale25_scale25_scale2_dt_vr.html) |
| 35–39 | 0248 | 25 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0248_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0248_scale25_scale25_scale2_dt_vr.html) |
| 18–19 | 0262 | 25 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0262_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0262_scale25_scale25_scale2_dt_vr.html) |
| 30–34 | 0275 | 70 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0275_scale70_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0275_scale70_scale25_scale2_dt_vr.html) |
| 75–79 | 0276 | 25 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0276_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0276_scale25_scale25_scale2_dt_vr.html) |
| 18–19 | 0290 | 25 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0290_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0290_scale25_scale25_scale2_dt_vr.html) |
| 80–84 | 0312 | 25 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0312_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0312_scale25_scale25_scale2_dt_vr.html) |
| 40–44 | 0314 | 25 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0314_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0314_scale25_scale25_scale2_dt_vr.html) |
| 45–49 | 0395 | 30 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0395_scale30_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0395_scale30_scale25_scale2_dt_vr.html) |
| 50–54 | 0401 | 35 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0401_scale35_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0401_scale35_scale25_scale2_dt_vr.html) |
| 65–69 | 0413 | 35 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0413_scale35_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0413_scale35_scale25_scale2_dt_vr.html) |
| 55–59 | 0420 | 35 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0420_scale35_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0420_scale35_scale25_scale2_dt_vr.html) |
| 18–19 | 0465 | 70 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0465_scale70_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0465_scale70_scale25_scale2_dt_vr.html) |
| 25–29 | 0515 | 35 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0515_scale35_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0515_scale35_scale25_scale2_dt_vr.html) |
| 18–19 | 0697 | 25 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0697_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0697_scale25_scale25_scale2_dt_vr.html) |
| 18–19 | 0886 | 25 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0886_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0886_scale25_scale25_scale2_dt_vr.html) |
| 80–84 | 0889 | 35 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0889_scale35_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0889_scale35_scale25_scale2_dt_vr.html) |
| 35–39 | 0897 | 25 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0897_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0897_scale25_scale25_scale2_dt_vr.html) |
| 85–92 | 0912 | 35 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0912_scale35_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0912_scale35_scale25_scale2_dt_vr.html) |
| 50–54 | 0936 | 25 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0936_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0936_scale25_scale25_scale2_dt_vr.html) |
| 60–64 | 0942 | 25 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0942_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_0942_scale25_scale25_scale2_dt_vr.html) |
| 30–34 | 1053 | 25 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_1053_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_1053_scale25_scale25_scale2_dt_vr.html) |
| 18–19 | 1088 | 25 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_1088_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_1088_scale25_scale25_scale2_dt_vr.html) |
| 20–24 | 1112 | 50 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_1112_scale50_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/aging/vr/ska3_ecg_1112_scale50_scale25_scale2_dt_vr.html) |

## Cubes — PTB

PhysioNet PTB Diagnostic ECG Database, lead II, 1000 Hz. One cube per record: third-order learning (scale 2) of its second-order run (scale 25), first order at scale 25. Axes z₃, ż₃ and P₃ or Δt₃ (time between two cycles); colour = the sign of v₃ = (P₂_k − P₂_k−1)/P₂_k−1 · c₃.

### Healthy controls, under 40

| age | record | P₃ cube | Δt₃ cube |
|---|---|---|---|
| 22 | ptb185 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb185_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb185_scale25_scale25_scale2_dt_vr.html) |
| 25 | ptb236 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb236_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb236_scale25_scale25_scale2_dt_vr.html) |
| 28 | ptb242 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb242_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb242_scale25_scale25_scale2_dt_vr.html) |
| 32 | ptb105 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb105_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb105_scale25_scale25_scale2_dt_vr.html) |
| 35 | ptb279 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb279_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb279_scale25_scale25_scale2_dt_vr.html) |

### Healthy controls, 40 and over

| age | sex | record | P₃ cube | Δt₃ cube |
|---|---|---|---|---|
| 40 | male | ptb251 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb251_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb251_scale25_scale25_scale2_dt_vr.html) |
| 44 | male | ptb244 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb244_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb244_scale25_scale25_scale2_dt_vr.html) |
| 45 | male | ptb264 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb264_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb264_scale25_scale25_scale2_dt_vr.html) |
| 47 | male | ptb237 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb237_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb237_scale25_scale25_scale2_dt_vr.html) |
| 48 | female | ptb247 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb247_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb247_scale25_scale25_scale2_dt_vr.html) |
| 48 | male | ptb284 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb284_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb284_scale25_scale25_scale2_dt_vr.html) |
| 50 | male | ptb172 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb172_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb172_scale25_scale25_scale2_dt_vr.html) |
| 52 | female | ptb243 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb243_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb243_scale25_scale25_scale2_dt_vr.html) |
| 54 | female | ptb169 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb169_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb169_scale25_scale25_scale2_dt_vr.html) |
| 54 | male | ptb116 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb116_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb116_scale25_scale25_scale2_dt_vr.html) |
| 54 | male | ptb246 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb246_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb246_scale25_scale25_scale2_dt_vr.html) |
| 54 | male | ptb252 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb252_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb252_scale25_scale25_scale2_dt_vr.html) |
| 55 | male | ptb229 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb229_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb229_scale25_scale25_scale2_dt_vr.html) |
| 57 | female | ptb173 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb173_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb173_scale25_scale25_scale2_dt_vr.html) |
| 58 | male | ptb104 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb104_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb104_scale25_scale25_scale2_dt_vr.html) |
| 59 | male | ptb239 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb239_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb239_scale25_scale25_scale2_dt_vr.html) |
| 64 | male | ptb248 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb248_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb248_scale25_scale25_scale2_dt_vr.html) |
| 67 | female | ptb267 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb267_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb267_scale25_scale25_scale2_dt_vr.html) |
| 68 | male | ptb122 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb122_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb122_scale25_scale25_scale2_dt_vr.html) |
| 68 | male | ptb266 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb266_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb266_scale25_scale25_scale2_dt_vr.html) |
| 69 | female | ptb121 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb121_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb121_scale25_scale25_scale2_dt_vr.html) |
| 69 | male | ptb255 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb255_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb255_scale25_scale25_scale2_dt_vr.html) |
| 81 | female | ptb184 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb184_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb184_scale25_scale25_scale2_dt_vr.html) |

### Myocardial infarction, women

| patient | age | infarction | when | record | P₃ cube | Δt₃ cube |
|---|---|---|---|---|---|---|
| 049 | 42 | inferior | day 0 | ptb049_s0173 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb049_s0173_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb049_s0173_scale25_scale25_scale2_dt_vr.html) |
| 049 | 42 | inferior | day 4 | ptb049_s0178 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb049_s0178_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb049_s0178_scale25_scale25_scale2_dt_vr.html) |
| 049 | 42 | inferior | day 11 | ptb049_s0186 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb049_s0186_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb049_s0186_scale25_scale25_scale2_dt_vr.html) |
| 049 | 42 | inferior | day 444 | ptb049_s0314 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb049_s0314_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb049_s0314_scale25_scale25_scale2_dt_vr.html) |
| 051 | 55 | antero-septal | day 0 | ptb051_s0179 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb051_s0179_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb051_s0179_scale25_scale25_scale2_dt_vr.html) |
| 051 | 55 | antero-septal | day 4 | ptb051_s0181 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb051_s0181_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb051_s0181_scale25_scale25_scale2_dt_vr.html) |
| 051 | 55 | antero-septal | day 10 | ptb051_s0187 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb051_s0187_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb051_s0187_scale25_scale25_scale2_dt_vr.html) |
| 051 | 55 | antero-septal | day 112 | ptb051_s0213 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb051_s0213_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb051_s0213_scale25_scale25_scale2_dt_vr.html) |
| 085 | 56 | posterior | day 0 | ptb085_s0296 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb085_s0296_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb085_s0296_scale25_scale25_scale2_dt_vr.html) |
| 085 | 56 | posterior | day 5 | ptb085_s0297 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb085_s0297_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb085_s0297_scale25_scale25_scale2_dt_vr.html) |
| 085 | 56 | posterior | day 11 | ptb085_s0298 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb085_s0298_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb085_s0298_scale25_scale25_scale2_dt_vr.html) |
| 085 | 56 | posterior | day 145 | ptb085_s0345 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb085_s0345_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb085_s0345_scale25_scale25_scale2_dt_vr.html) |
| 098 | 63 | inferior | day 0 | ptb098_s0386 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb098_s0386_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb098_s0386_scale25_scale25_scale2_dt_vr.html) |
| 098 | 63 | inferior | day 5 | ptb098_s0389 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb098_s0389_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb098_s0389_scale25_scale25_scale2_dt_vr.html) |
| 098 | 63 | inferior | day 23 | ptb098_s0398 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb098_s0398_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb098_s0398_scale25_scale25_scale2_dt_vr.html) |
| 098 | 63 | inferior | day 30 | ptb098_s0409 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb098_s0409_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb098_s0409_scale25_scale25_scale2_dt_vr.html) |
| 046 | 64 | antero-septal | day 0 | ptb046_s0156 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb046_s0156_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb046_s0156_scale25_scale25_scale2_dt_vr.html) |
| 046 | 64 | antero-septal | day 2 | ptb046_s0161 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb046_s0161_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb046_s0161_scale25_scale25_scale2_dt_vr.html) |
| 046 | 64 | antero-septal | day 12 | ptb046_s0168 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb046_s0168_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb046_s0168_scale25_scale25_scale2_dt_vr.html) |
| 046 | 64 | antero-septal | day 37 | ptb046_s0184 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb046_s0184_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb046_s0184_scale25_scale25_scale2_dt_vr.html) |
| 086 | 66 | infero-lateral | day 0 | ptb086_s0316 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb086_s0316_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb086_s0316_scale25_scale25_scale2_dt_vr.html) |
| 100 | 72 | inferior | day 0 | ptb100_s0399 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb100_s0399_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb100_s0399_scale25_scale25_scale2_dt_vr.html) |
| 100 | 72 | inferior | day 3 | ptb100_s0401 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb100_s0401_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb100_s0401_scale25_scale25_scale2_dt_vr.html) |
| 100 | 72 | inferior | day 7 | ptb100_s0407 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb100_s0407_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb100_s0407_scale25_scale25_scale2_dt_vr.html) |
| 091 | 78 | antero-septal | day 0 | ptb091_s0353 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb091_s0353_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb091_s0353_scale25_scale25_scale2_dt_vr.html) |
| 091 | 78 | antero-septal | day 4 | ptb091_s0357 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb091_s0357_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb091_s0357_scale25_scale25_scale2_dt_vr.html) |
| 091 | 78 | antero-septal | day 11 | ptb091_s0361 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb091_s0361_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb091_s0361_scale25_scale25_scale2_dt_vr.html) |
| 091 | 78 | antero-septal | day 78 | ptb091_s0408 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb091_s0408_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb091_s0408_scale25_scale25_scale2_dt_vr.html) |

### Myocardial infarction, men

| patient | age | infarction | when | record | P₃ cube | Δt₃ cube |
|---|---|---|---|---|---|---|
| 035 | 40 | inferior | day 0 | ptb035_s0110 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb035_s0110_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb035_s0110_scale25_scale25_scale2_dt_vr.html) |
| 035 | 40 | inferior | day 5 | ptb035_s0119 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb035_s0119_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb035_s0119_scale25_scale25_scale2_dt_vr.html) |
| 035 | 40 | inferior | day 63 | ptb035_s0145 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb035_s0145_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb035_s0145_scale25_scale25_scale2_dt_vr.html) |
| 054 | 47 | infero-lateral | day 0 | ptb054_s0192 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb054_s0192_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb054_s0192_scale25_scale25_scale2_dt_vr.html) |
| 054 | 47 | infero-lateral | day 3 | ptb054_s0195 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb054_s0195_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb054_s0195_scale25_scale25_scale2_dt_vr.html) |
| 054 | 47 | infero-lateral | day 10 | ptb054_s0197 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb054_s0197_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb054_s0197_scale25_scale25_scale2_dt_vr.html) |
| 032 | 49 | antero-septal | day 0 | ptb032_s0102 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb032_s0102_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb032_s0102_scale25_scale25_scale2_dt_vr.html) |
| 032 | 49 | antero-septal | day 4 | ptb032_s0106 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb032_s0106_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb032_s0106_scale25_scale25_scale2_dt_vr.html) |
| 032 | 49 | antero-septal | day 11 | ptb032_s0115 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb032_s0115_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb032_s0115_scale25_scale25_scale2_dt_vr.html) |
| 032 | 49 | antero-septal | day 98 | ptb032_s0165 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb032_s0165_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb032_s0165_scale25_scale25_scale2_dt_vr.html) |
| 065 | 52 | infero-postero-lateral | day 0 | ptb065_s0221 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb065_s0221_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb065_s0221_scale25_scale25_scale2_dt_vr.html) |
| 065 | 52 | infero-postero-lateral | day 5 | ptb065_s0226 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb065_s0226_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb065_s0226_scale25_scale25_scale2_dt_vr.html) |
| 065 | 52 | infero-postero-lateral | day 7 | ptb065_s0229 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb065_s0229_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb065_s0229_scale25_scale25_scale2_dt_vr.html) |
| 065 | 52 | infero-postero-lateral | day 194 | ptb065_s0282 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb065_s0282_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb065_s0282_scale25_scale25_scale2_dt_vr.html) |
| 099 | 52 | antero-lateral | day 0 | ptb099_s0387 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb099_s0387_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb099_s0387_scale25_scale25_scale2_dt_vr.html) |
| 099 | 52 | antero-lateral | day 4 | ptb099_s0388 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb099_s0388_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb099_s0388_scale25_scale25_scale2_dt_vr.html) |
| 099 | 52 | antero-lateral | day 22 | ptb099_s0397 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb099_s0397_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb099_s0397_scale25_scale25_scale2_dt_vr.html) |
| 099 | 52 | antero-lateral | day 91 | ptb099_s0419 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb099_s0419_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb099_s0419_scale25_scale25_scale2_dt_vr.html) |
| 088 | 54 | inferior | day 0 | ptb088_s0339 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb088_s0339_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb088_s0339_scale25_scale25_scale2_dt_vr.html) |
| 088 | 54 | inferior | day 7 | ptb088_s0352 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb088_s0352_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb088_s0352_scale25_scale25_scale2_dt_vr.html) |
| 088 | 54 | inferior | day 92 | ptb088_s0413 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb088_s0413_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb088_s0413_scale25_scale25_scale2_dt_vr.html) |
| 084 | 55 | antero-septal | day 0 | ptb084_s0281 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb084_s0281_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb084_s0281_scale25_scale25_scale2_dt_vr.html) |
| 084 | 55 | antero-septal | day 6 | ptb084_s0288 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb084_s0288_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb084_s0288_scale25_scale25_scale2_dt_vr.html) |
| 084 | 55 | antero-septal | day 7 | ptb084_s0289 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb084_s0289_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb084_s0289_scale25_scale25_scale2_dt_vr.html) |
| 084 | 55 | antero-septal | day 127 | ptb084_s0313 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb084_s0313_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb084_s0313_scale25_scale25_scale2_dt_vr.html) |
| 077 | 65 | inferior | day 0 | ptb077_s0251 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb077_s0251_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb077_s0251_scale25_scale25_scale2_dt_vr.html) |
| 077 | 65 | inferior | day 5 | ptb077_s0254 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb077_s0254_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb077_s0254_scale25_scale25_scale2_dt_vr.html) |
| 077 | 65 | inferior | day 9 | ptb077_s0258 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb077_s0258_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb077_s0258_scale25_scale25_scale2_dt_vr.html) |
| 077 | 65 | inferior | day 43 | ptb077_s0285 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb077_s0285_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb077_s0285_scale25_scale25_scale2_dt_vr.html) |
| 082 | 65 | antero-septal | day 0 | ptb082_s0267 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb082_s0267_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb082_s0267_scale25_scale25_scale2_dt_vr.html) |
| 082 | 65 | antero-septal | day 3 | ptb082_s0271 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb082_s0271_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb082_s0271_scale25_scale25_scale2_dt_vr.html) |
| 082 | 65 | antero-septal | day 8 | ptb082_s0279 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb082_s0279_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb082_s0279_scale25_scale25_scale2_dt_vr.html) |
| 082 | 65 | antero-septal | day 142 | ptb082_s0320 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb082_s0320_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb082_s0320_scale25_scale25_scale2_dt_vr.html) |
| 087 | 66 | infero-postero-lateral | day 0 | ptb087_s0321 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb087_s0321_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb087_s0321_scale25_scale25_scale2_dt_vr.html) |
| 087 | 66 | infero-postero-lateral | day 4 | ptb087_s0326 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb087_s0326_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb087_s0326_scale25_scale25_scale2_dt_vr.html) |
| 087 | 66 | infero-postero-lateral | day 9 | ptb087_s0330 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb087_s0330_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb087_s0330_scale25_scale25_scale2_dt_vr.html) |
| 078 | 68 | inferior | day 0 | ptb078_s0255 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb078_s0255_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb078_s0255_scale25_scale25_scale2_dt_vr.html) |
| 078 | 68 | inferior | day 2 | ptb078_s0259 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb078_s0259_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb078_s0259_scale25_scale25_scale2_dt_vr.html) |
| 078 | 68 | inferior | day 9 | ptb078_s0262 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb078_s0262_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb078_s0262_scale25_scale25_scale2_dt_vr.html) |
| 078 | 68 | inferior | day 167 | ptb078_s0317 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb078_s0317_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb078_s0317_scale25_scale25_scale2_dt_vr.html) |
| 097 | 68 | anterior | day 0 | ptb097_s0380 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb097_s0380_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb097_s0380_scale25_scale25_scale2_dt_vr.html) |
| 097 | 68 | anterior | day 3 | ptb097_s0382 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb097_s0382_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb097_s0382_scale25_scale25_scale2_dt_vr.html) |
| 097 | 68 | anterior | day 10 | ptb097_s0384 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb097_s0384_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb097_s0384_scale25_scale25_scale2_dt_vr.html) |
| 097 | 68 | anterior | day 34 | ptb097_s0394 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb097_s0394_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb097_s0394_scale25_scale25_scale2_dt_vr.html) |
| 023 | 69 | inferior | day 0 | ptb023_s0080 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb023_s0080_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb023_s0080_scale25_scale25_scale2_dt_vr.html) |
| 023 | 69 | inferior | day 2 | ptb023_s0081 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb023_s0081_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb023_s0081_scale25_scale25_scale2_dt_vr.html) |
| 023 | 69 | inferior | day 11 | ptb023_s0085 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb023_s0085_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb023_s0085_scale25_scale25_scale2_dt_vr.html) |
| 023 | 69 | inferior | day 31 | ptb023_s0103 | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb023_s0103_scale25_scale25_scale2_vr.html) | [open](https://quantiota.github.io/SKA-ECG-Third-Order/ptb/vr/ska3_ecg_ptb023_s0103_scale25_scale25_scale2_dt_vr.html) |

## Run

```bash
cd scripts
python plot_third_order.py aging 0060 25 25 2      # figure
python build_cube3.py aging 0060 25 25 2           # cube, vertical axis P₃
python build_cube3.py aging 0060 25 25 2 dt        # cube, vertical axis Δt₃ (time between two cycles)
```

The SKA learner itself is not included in this repository.

## License

Scripts: MIT. ECG data: PhysioNet, under the license of each database.
