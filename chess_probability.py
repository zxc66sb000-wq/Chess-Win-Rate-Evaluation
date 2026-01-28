
#!/usr/bin/env python3 & # -*- coding: utf-8 -*-

import math

def sigmoid(x):
    """📊 Sigmoid function"""
    return 1 / (1 + math.exp(-x))

def calculate_K(R_avg):
    """🎯 Evaluation → Elo conversion"""
    return 50 + 150 * sigmoid((R_avg - 1800) / 400)

def calculate_D_base(R_avg):
    """🤝 Base draw rate"""
    return 0.20 + 0.30 * sigmoid((R_avg - 1800) / 500)

def calculate_probabilities(R_w, R_b, E_pawn):
    """🧮 Calculate win/draw/loss probabilities"""
    R_avg = (R_w + R_b) / 2
    delta_R_0 = R_w - R_b
    
    K = calculate_K(R_avg)
    delta_R_eval = E_pawn * K
    delta_R_eff = delta_R_0 + delta_R_eval
    
    S_w = 1 / (1 + 10 ** (-delta_R_eff / 400))
    D_base = calculate_D_base(R_avg)
    
    decay1 = math.exp(-abs(delta_R_eff) / 600)
    decay2 = math.exp(-abs(E_pawn) ** 1.5 / 3)
    alpha = decay1 * decay2
    
    P_draw_raw = D_base * (0.3 + 0.7 * alpha)
    P_draw = max(0.05, min(0.65, P_draw_raw))
    
    P_w_unnorm = max(0, S_w - 0.5 * P_draw)
    P_b_unnorm = max(0, (1 - S_w) - 0.5 * P_draw)
    
    total = P_w_unnorm + P_draw + P_b_unnorm
    P_w = P_w_unnorm / total
    P_draw = P_draw / total
    P_b = P_b_unnorm / total
    
    return P_w, P_draw, P_b

def print_probability_bar(p_w, p_draw, p_b):
    """🎨 Visual probability bar"""
    w = int(p_w * 30)
    d = int(p_draw * 30)
    b = int(p_b * 30)
    return "🎲 [" + "♔"*w + "🤝"*d + "♚"*b + "]"

def print_eval_emoji(E_pawn):
    """📊 Evaluation emoji indicator"""
    if E_pawn > 0:
        if abs(E_pawn) < 0.5: return "⚖️  ♔ slightly better"
        elif abs(E_pawn) < 1.5: return "👍 ♔ clearly better"
        elif abs(E_pawn) < 3.0: return "🔥 ♔ decisive"
        else: return "🏆 ♔ crushing"
    elif E_pawn < 0:
        if abs(E_pawn) < 0.5: return "⚖️  ♚ slightly better"
        elif abs(E_pawn) < 1.5: return "👍 ♚ clearly better"
        elif abs(E_pawn) < 3.0: return "🔥 ♚ decisive"
        else: return "🏆 ♚ crushing"
    else: return "⚖️  balanced"

def main():
    print("♔♚♔♚♔♚♔♚♔♚♔♚♔♚♔♚")
    print("♟️ Chess Win Probability Calculator")
    print("♔♚♔♚♔♚♔♚♔♚♔♚♔♚♔♚\n")
    
    try:
        R_w = float(input("♔ White's Elo: "))
        R_b = float(input("♚ Black's Elo: "))
    except ValueError:
        print("❌ Invalid input!")
        return
    
    print("\n📊 Initial (evaluation = 0):")
    P_w, P_draw, P_b = calculate_probabilities(R_w, R_b, 0)
    print(f"♔ Wins: {P_w*100:6.1f}%  🤝 Draw: {P_draw*100:6.1f}%  ♚ Wins: {P_b*100:6.1f}%")
    print(print_probability_bar(P_w, P_draw, P_b))
    
    print("\n♟️ Enter evaluation (♔+/♚-, e.g., +1.50):")
    print("🎯 Press Enter to exit\n")
    
    while True:
        try:
            E_input = input("📊 Eval: ").strip()
            if E_input == "": break
            
            E_pawn = float(E_input)
            P_w, P_draw, P_b = calculate_probabilities(R_w, R_b, E_pawn)
            
            print(f"\n📈 {E_pawn:+.2f} pawns → {print_eval_emoji(E_pawn)}")
            print(f"♔ Wins: {P_w*100:6.1f}%  🤝 Draw: {P_draw*100:6.1f}%  ♚ Wins: {P_b*100:6.1f}%")
            print(print_probability_bar(P_w, P_draw, P_b))
            
            if P_w > 0.75: print("   🎯 ♔ dominating!")
            elif P_b > 0.75: print("   🎯 ♚ dominating!")
            elif P_draw > 0.5: print("   🎯 high draw chance")
            
        except ValueError:
            print("❌ Please enter a number")
        except KeyboardInterrupt:
            print("\n♟️ Goodbye!")
            break

if __name__ == "__main__":
    main()
