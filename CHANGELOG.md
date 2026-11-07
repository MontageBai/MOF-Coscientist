# Changelog

## 2.0.0 — 2026-11-07

### Added

- Promote the October `mof-tandem-bed-co-scientist` package to the primary skill for general multicomponent tandem-bed design.
- Executable capacity matching: common upstream breakthrough cutoff, dynamic retention integration, residual downstream duties, and componentwise controlling mass ratio.
- Explicit ordinary-time versus mass-normalized-coordinate handling, raw-curve quality flags, experimental discrepancy records, and separate feed-transfer scenarios.
- Input manifest protocol, evidence-based material corrections, and updated Chinese entry guidance.
- A synthetic CSV example and numerical regression checks; synthetic data are not experimental validation.
- Version metadata, dependency list, and installation instructions for Windows, macOS, and Linux.

### Corrected during packaging

- Route the reusable prompt to the tandem equations and use the new skill name in forward-test instructions.
- Reject nonfinite mass/load/transfer inputs and ambiguous duplicate or overlapping duty groups before calculating a mass ratio.
- Require at least one downstream candidate for capacity matching.

### Compatibility and limits

- The July `mof-separation-co-scientist` export remains unchanged for historical reproduction. See `CHANGELOG_BRIEF.md` for its original notes.
- No new project-specific experimental results or blind-test outcomes are added to the active skill.
- Calculated ratios are capacity-matching baselines, not validated global optima. Feed transfer remains assumption-dependent when matched dynamic data are unavailable.
- Structure and synthetic numerical checks do not establish scientific superiority or real-process performance.
