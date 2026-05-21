#!/usr/bin/env python3
"""
简单演示：用 Agent 生成的 CLI 工具
用途：计算以太坊地址的 checksum（校验和）格式

这是模块 A 的实践成果之一 - 让 Agent 生成一个小工具
"""

import hashlib
import re


def to_checksum_address(address: str) -> str:
    """
    将以太坊地址转换为 Checksum 格式
    
    原理（EIP-55）:
    1. 去掉 0x 前缀，转为小写
    2. 计算 Keccak-256 哈希
    3. 对每个十六进制字符：
       - 如果是 a-f，且哈希对应位 >= 8，转大写
       - 否则保持小写
    
    Args:
        address: 以太坊地址（带或不带 0x 前缀）
    
    Returns:
        Checksum 格式的地址（大小写混合）
    
    Example:
        >>> to_checksum_address("0x5af0d9827e0c53e4799bb226655a1de152a425a5")
        '0x5Af0D9827E0c53E4799Bb226655A1De152A425a5'
    """
    # 去掉 0x 前缀
    address = address.replace("0x", "").lower()
    
    # 验证地址格式
    if not re.match(r'^[0-9a-f]{40}$', address):
        raise ValueError("Invalid Ethereum address format")
    
    # 计算 hash
    address_hash = hashlib.sha3_256(address.encode()).hexdigest()
    
    # 生成 checksum 地址
    checksum_address = ""
    for i, char in enumerate(address):
        if char in "0123456789":
            checksum_address += char
        else:
            # 检查 hash 对应位是否 >= 8
            if int(address_hash[i], 16) >= 8:
                checksum_address += char.upper()
            else:
                checksum_address += char
    
    return "0x" + checksum_address


def validate_checksum_address(address: str) -> bool:
    """
    验证地址是否为有效的 Checksum 格式
    
    Args:
        address: 待验证的地址
    
    Returns:
        True 如果是正确的 checksum 格式，False  otherwise
    """
    expected = to_checksum_address(address)
    return expected.lower().startswith("0x") and expected == address


def main():
    """CLI 主函数"""
    print("=" * 60)
    print("🔐 Ethereum Address Checksum Converter (EIP-55)")
    print("=" * 60)
    
    while True:
        user_input = input("\n请输入以太坊地址 (或输入 'q' 退出): ").strip()
        
        if user_input.lower() == 'q':
            print("再见！👋")
            break
        
        if not user_input:
            print("❌ 地址不能为空，请重新输入")
            continue
        
        try:
            checksum_addr = to_checksum_address(user_input)
            
            is_valid = validate_checksum_address(user_input)
            validity_mark = "✅" if is_valid else "⚠️  原地址非 Checksum 格式"
            
            print(f"\n{validity_mark}")
            print(f"原始地址: {user_input}")
            print(f"Checksum: {checksum_addr}")
            
        except ValueError as e:
            print(f"❌ 错误：{e}")
        except Exception as e:
            print(f"❌ 未知错误：{e}")


if __name__ == "__main__":
    main()
