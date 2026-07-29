import numpy as np

def run_gradient_demo(learning_rate=0.01, epochs=200):
    x = np.linspace(0, 10, 50)
    y = 2 * x + 1
    w = 0.0
    b = 0.0
    losses = []
    for _ in range(epochs):
        pred = w * x + b
        loss = np.mean((pred - y) ** 2)
        losses.append(float(loss))
        dw = np.mean(2 * (pred - y) * x)
        db = np.mean(2 * (pred - y))
        w -= learning_rate * dw
        b -= learning_rate * db
    return {
        "learning_rate": learning_rate,
        "epochs": epochs,
        "losses": losses,
        "final_parameters": {"w": float(w), "b": float(b)}
    }
