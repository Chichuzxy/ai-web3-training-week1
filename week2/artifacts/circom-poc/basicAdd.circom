pragma circom 2.2.3

template BasicAdd() {
    signal input a;
    signal input b;
    signal output c;

    // 约束条件：c 必须等于 a + b
    c <== a + b;
}

// 实例化模板
component main = BasicAdd();