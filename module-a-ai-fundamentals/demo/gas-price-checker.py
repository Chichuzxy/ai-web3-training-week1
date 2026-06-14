#!/usr/bin/env python3
"""
简单演示 2：用 Agent 生成的 Gas Price 查询工具
用途：通过公开 Ethereum RPC 接口查询当前 Gas 价格

这是模块 A 的第二个实践成果 - 让 Agent 生成一个连接真实链上数据的小工具
注意：只读操作，不需要钱包签名，适合测试网和主网
"""

import json
import time
from urllib.request import Request, urlopen
from urllib.error import URLError


# 公开以太坊 RPC 端点（无认证要求），按优先级排列
RPC_ENDPOINTS = {
    "mainnet": [
        "https://eth.llamarpc.com",
        "https://rpc.ankr.com/eth",
        "https://ethereum-rpc.publicnode.com",
    ],
    "sepolia": [
        "https://rpc.sepolia.org",
        "https://rpc-sepolia.rockx.com",
        "https://ethereum-sepolia-rpc.publicnode.com",
    ],
}


def call_rpc(endpoint: str, method: str, params: list = None) -> dict:
    """
    向以太坊节点发送 JSON-RPC 请求
    
    Args:
        endpoint: RPC 端点 URL
        method: RPC 方法名（如 eth_gasPrice）
        params: 方法参数列表
    
    Returns:
        RPC 响应字典
    """
    payload = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params or [],
        "id": int(time.time() * 1000)  # 唯一请求 ID
    }
    
    req = Request(
        endpoint,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "User-Agent": "Web3TrainingWeek1/1.0"
        }
    )
    
    try:
        response = urlopen(req, timeout=10)
        result = json.loads(response.read().decode("utf-8"))
        return result.get("result", {})
    except URLError as e:
        raise ConnectionError(f"RPC 请求失败：{e}")


def gwei_from_wei(wei: int) -> float:
    """将 Wei 转换为 Gwei（1 Gwei = 10^9 Wei）"""
    return wei / 1e9


def _call_rpc_with_fallback(endpoints: list, method: str, params: list = None) -> dict:
    """尝试多个 RPC 端点，第一个成功的返回"""
    for endpoint in endpoints:
        try:
            result = call_rpc(endpoint, method, params)
            return result
        except ConnectionError:
            continue
    raise ConnectionError(f"所有 RPC 端点均不可用（已尝试 {len(endpoints)} 个）")


def get_gas_price(network: str = "sepolia") -> dict:
    """
    获取指定网络的 Gas 价格
    
    Args:
        network: 网络名称 ("mainnet" 或 "sepolia")
    
    Returns:
        包含 gas_price (gwei) 和 block_number 的字典
    """
    if network not in RPC_ENDPOINTS:
        raise ValueError(f"不支持的网络：{network}。可选值：{list(RPC_ENDPOINTS.keys())}")
    
    endpoints = RPC_ENDPOINTS[network]
    
    # 使用回退机制获取 Gas 价格
    hex_price = _call_rpc_with_fallback(endpoints, "eth_gasPrice")
    gas_price_gwei = gwei_from_wei(int(hex_price, 16))
    
    # 获取最新区块号
    hex_block = _call_rpc_with_fallback(endpoints, "eth_blockNumber")
    block_number = int(hex_block, 16)
    
    return {
        "gas_price_gwei": round(gas_price_gwei, 2),
        "block_number": block_number,
        "network": network
    }


def estimate_gas_cost(tx_type: str = "standard", network: str = "sepolia") -> dict:
    """
    估算不同类型交易的 Gas 消耗和费用
    
    Gas 用量参考值：
    - 普通转账 (ETH transfer): 21,000 gas
    - ERC-20 转账: ~65,000 gas
    - 简单合约交互: ~50,000 gas
    - 复杂合约部署: 500,000+ gas
    
    Args:
        tx_type: 交易类型
        network: 网络名称
    
    Returns:
        预估费用信息
    """
    gas_costs = {
        "simple_transfer": {"name": "简单 ETH 转账", "gas_limit": 21000},
        "erc20_transfer": {"name": "ERC-20 Token 转账", "gas_limit": 65000},
        "standard_contract": {"name": "标准合约调用", "gas_limit": 50000},
        "complex_deploy": {"name": "复杂合约部署", "gas_limit": 500000},
    }
    
    if tx_type not in gas_costs:
        available = ", ".join(gas_costs.keys())
        raise ValueError(f"未知交易类型 '{tx_type}'。可用类型：{available}")
    
    gas_info = gas_costs[tx_type]
    gas_data = get_gas_price(network)
    
    # 用回退机制获取最新的 gasPrice
    hex_price = _call_rpc_with_fallback(RPC_ENDPOINTS[network], "eth_gasPrice")
    total_cost_wei = gas_info["gas_limit"] * int(hex_price, 16)
    total_cost_eth = total_cost_wei / 1e18
    total_cost_gwei = gas_info["gas_limit"] * gas_data["gas_price_gwei"]
    
    return {
        "type": gas_info["name"],
        "gas_limit": gas_info["gas_limit"],
        "gas_price_gwei": gas_data["gas_price_gwei"],
        "estimated_cost_eth": round(total_cost_eth, 8),
        "estimated_cost_gwei_total": round(total_cost_gwei, 2),
        "network": network,
        "block_number": gas_data["block_number"]
    }


def main():
    """CLI 主函数"""
    print("=" * 60)
    print("⛽ Web3 Gas Price Checker")
    print("=" * 60)
    print()
    print("可用网络:")
    for net, url in RPC_ENDPOINTS.items():
        print(f"  - {net}: {url}")
    print()
    
    while True:
        print("-" * 40)
        print('输入 "q" 退出')
        print('输入 "quick" 快速查看 Sepolia 当前 Gas')
        print('输入 "cost [类型]" 估算某类交易费用')
        print('  类型可选: simple_transfer, erc20_transfer, standard_contract, complex_deploy')
        
        user_input = input("\n> ").strip()
        
        if user_input.lower() == 'q':
            print("再见！")
            break
        
        if user_input.lower() == 'quick':
            try:
                info = get_gas_price("sepolia")
                print(f"\n✅ Sepolia 测试网当前 Gas 价格: {info['gas_price_gwei']} Gwei")
                print(f"   最新区块号: #{info['block_number']}")
            except ConnectionError as e:
                print(f"\n❌ 网络连接失败：{e}")
                print("   请稍后重试，或换一个 RPC 端点")
            continue
        
        if user_input.lower().startswith('cost'):
            parts = user_input.split()
            if len(parts) < 2:
                print("❌ 请指定交易类型，例如：cost simple_transfer")
                continue
            
            tx_type = parts[1]
            try:
                result = estimate_gas_cost(tx_type)
                print(f"\n{'=' * 50}")
                print(f"📊 费用估算：{result['type']}")
                print(f"{'=' * 50}")
                print(f"  Gas 限制:     {result['gas_limit']:,}")
                print(f"  Gas 单价:     {result['gas_price_gwei']} Gwei")
                print(f"  总费用:       {result['estimated_cost_gwei_total']:,.2f} Gwei")
                print(f"  折合 ETH:     {result['estimated_cost_eth']} ETH")
                print(f"  网络:         {result['network']}")
                print(f"  区块号:       #{result['block_number']}")
                print(f"{'=' * 50}")
            except (ValueError, ConnectionError) as e:
                print(f"\n❌ 错误：{e}")
            continue
        
        print("❌ 无效输入，请重新选择")


if __name__ == "__main__":
    main()
