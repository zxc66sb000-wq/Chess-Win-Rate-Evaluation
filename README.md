# Chess Win Probability Calculator ♟️

## Overview
A Python tool that calculates chess win/draw/loss probabilities based on player Elo ratings and engine evaluation scores. This calculator incorporates sophisticated modeling of draw rates and evaluation impact to provide realistic probability estimates for chess positions.

## Features
- **Elo-based probability calculation** - Converts Elo differences to win probabilities
- **Evaluation integration** - Incorporates engine evaluation (in pawns) into probability calculations
- **Dynamic draw rate modeling** - Draw probability varies with average Elo and position sharpness
- **Visual probability bars** - ASCII-art style visualization of probabilities
- **Evaluation interpretation** - Provides human-readable descriptions of evaluation scores
- **Interactive interface** - Real-time calculation with user inputs

## Mathematical Model

### Core Components
1. **Sigmoid Function**: Used for smooth transitions between rating effects
2. **Evaluation-to-Elo Conversion**: Converts engine evaluation (pawns) to equivalent Elo points
3. **Base Draw Rate**: Models draw probability based on average player strength
4. **Dynamic Decay Factors**: Adjust draw probability based on position sharpness

### Key Formulas
- **Effective Rating Difference**: `ΔR_eff = (R_white - R_black) + K × E_pawn`
- **Win Probability**: `P_win = 1 / (1 + 10^(-ΔR_eff/400))`
- **Draw Probability**: Adjusts based on position complexity and player strength
- **Normalization**: Ensures probabilities sum to 100%

## Installation & Usage

### Requirements
- Python 3.x
- No external dependencies

### Running the Calculator
```bash
python chess_probability.py
```

### Interactive Usage
1. Enter White's Elo rating
2. Enter Black's Elo rating
3. View initial probabilities (evaluation = 0)
4. Enter engine evaluations in pawns (e.g., +1.50, -0.75)
5. Press Enter to exit

## Evaluation Interpretation
- **0.00-0.49**: ⚖️ Slight advantage
- **0.50-1.49**: 👍 Clear advantage
- **1.50-2.99**: 🔥 Decisive advantage
- **3.00+**: 🏆 Crushing advantage

## Example Output
```
♔♚♔♚♔♚♔♚♔♚♔♚♔♚♔♚
♟️ Chess Win Probability Calculator
♔♚♔♚♔♚♔♚♔♚♔♚♔♚♔♚

♔ White's Elo: 2700
♚ Black's Elo: 2600

📊 Initial (evaluation = 0):
♔ Wins:  64.1%  🤝 Draw:  25.5%  ♚ Wins:  10.4%
🎲 [♔♔♔♔♔♔♔♔♔♔♔♔♔♔♔♔♔♔🤝🤝🤝🤝🤝🤝♚♚♚]

📊 Eval: +1.50

📈 +1.50 pawns → 🔥 ♔ decisive
♔ Wins:  85.2%  🤝 Draw:  12.1%  ♚ Wins:   2.7%
🎲 [♔♔♔♔♔♔♔♔♔♔♔♔♔♔♔♔♔♔♔♔♔♔♔♔♔♔🤝🤝🤝♚]
   🎯 ♔ dominating!
```

## Functions

### Core Functions
- `calculate_probabilities(R_w, R_b, E_pawn)`: Main probability calculation
- `sigmoid(x)`: Mathematical sigmoid function
- `calculate_K(R_avg)`: Converts evaluation to Elo equivalent
- `calculate_D_base(R_avg)`: Calculates base draw rate

### Display Functions
- `print_probability_bar(p_w, p_draw, p_b)`: Creates visual probability bar
- `print_eval_emoji(E_pawn)`: Returns descriptive evaluation text with emoji

## Applications
- **Game analysis**: Understand position evaluation in probabilistic terms
- **Match prediction**: Estimate outcomes based on player ratings
- **Learning tool**: Visualize how evaluations translate to winning chances
- **Tournament planning**: Assess relative strengths and draw likelihoods

## Limitations
- Model assumes standard time controls
- Evaluation interpretation thresholds are approximate
- Draw rate model based on typical tournament statistics
- Assumes accurate engine evaluation

## License
Open source - free for educational and personal use.

---

♟️ *May your probabilities be ever in your favor!* ♟️
