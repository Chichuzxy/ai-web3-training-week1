# train_model.py - 训练线性回归 -> ONNX Gemm (归一化输入)
# ZKML Pipeline Agent: Day 1
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import onnx
from onnx import helper, TensorProto
import os

# 1. 生成 + 归一化
X, y = make_regression(n_samples=500, n_features=5, noise=0.1, random_state=42)
scaler_X = StandardScaler()
scaler_y = StandardScaler()
X_scaled = scaler_X.fit_transform(X)
y_scaled = scaler_y.fit_transform(y.reshape(-1, 1)).ravel()

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_scaled, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
score = model.score(X_test, y_test)
print(f"R2 score: {score:.4f}")
print(f"Coefficients: {model.coef_}")
print(f"Intercept: {model.intercept_:.4f}")

# 2. ONNX Gemm model
n_features = 5
coef = model.coef_.astype(np.float32).reshape(5, 1)
intercept = np.array([model.intercept_]).astype(np.float32).reshape(1, 1)

X_input = helper.make_tensor_value_info('float_input', TensorProto.FLOAT, [None, n_features])
Y_output = helper.make_tensor_value_info('variable', TensorProto.FLOAT, [None, 1])

gemm_node = helper.make_node('Gemm', inputs=['float_input', 'coef', 'intercept'],
    outputs=['variable'], alpha=1.0, beta=1.0, transB=0)

graph = helper.make_graph(
    nodes=[gemm_node], name='LinearRegression',
    inputs=[X_input], outputs=[Y_output],
    initializer=[
        helper.make_tensor('coef', TensorProto.FLOAT, [5, 1], coef.flatten().tolist()),
        helper.make_tensor('intercept', TensorProto.FLOAT, [1, 1], intercept.flatten().tolist())
    ]
)

onnx_model = helper.make_model(graph, opset_imports=[helper.make_opsetid('', 11)])
os.makedirs("project/models", exist_ok=True)
onnx.save(onnx_model, "project/models/model.onnx")
onnx.checker.check_model(onnx_model)
print("ONNX model saved: project/models/model.onnx")

# 3. 测试数据（用归一化后的小值）
y_pred = model.predict(X_test[:10])
np.savez("model_test_data.npz",
    X_test=X_test[:10].astype(np.float32),
    y_test=y_test[:10].astype(np.float32),
    y_pred=y_pred.astype(np.float32),
    coef=coef.flatten(),
    intercept=np.array([model.intercept_]),
    n_features=n_features
)

# 4. 验证
import onnxruntime as ort
sess = ort.InferenceSession("project/models/model.onnx")
for i in range(3):
    inp = X_test[i:i+1].astype(np.float32)
    out = sess.run(None, {'float_input': inp})[0]
    print(f"  [{i}] ONNX: {out[0][0]:.6f}, sklearn: {y_pred[i]:.6f}")
