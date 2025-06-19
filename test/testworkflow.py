from web3 import Web3
import dotenv
import os

dotenv.load_dotenv()

# ========== KONFIGURASI (Testnet) ==========
RPC_URL     = "https://sepolia.base.org"                   # RPC testnet Base Sepolia

CHAIN_ID    = 84532                                        # Chain ID testnet Base Sepolia
PRIVATE_KEY = os.getenv("TESNET_PRIVATE_KEY")
WALLET      = Web3(Web3.HTTPProvider(RPC_URL)).eth.account.from_key(PRIVATE_KEY).address

# Token testnet & bonding curve dummy (sudah tersedia!)
BONDING_ADDR = "0x4b28Cb156287028Aa34165FFDEc9fB680527378c"   # Gunakan contract testnet ini
AMOUNT_BASE  = 0.001                                       # Jumlah BASE testnet untuk beli (bebas diubah kecil/rawan rugi)

# ========== KONEKSI ==========
w3 = Web3(Web3.HTTPProvider(RPC_URL))

# --- CEK SALDO SEBELUM BUY---
balance_before = w3.eth.get_balance(WALLET)
print(f"Saldo sebelum buy: {w3.from_wei(balance_before, 'ether')} BASE (testnet)")

# --- SIMULASI TRANSAKSI (tidak kirim, hanya print!) ---
tx = {
    "from": WALLET,
    "to": BONDING_ADDR,
    "value": w3.to_wei(AMOUNT_BASE, 'ether'),
    "gas": 120000,
    "gasPrice": w3.to_wei(1, 'gwei'),
    "nonce": w3.eth.get_transaction_count(WALLET),
    "chainId": CHAIN_ID,
}
print("\\n[SIMULASI] Data transaksi buy:")
for k, v in tx.items():
    print(f"{k}: {v}")

try:
    estimated_gas = w3.eth.estimate_gas(tx)
    print("Estimasi gas:", estimated_gas)
    print("Estimasi biaya (BASE):", w3.from_wei(estimated_gas*tx['gasPrice'], 'ether'))
except Exception as e:
    print("Estimasi gas gagal:", str(e))

print("\\n=== SIMULASI: Tidak ada BASE keluar dompet TESTNET ===")

# === KIRIM TRANSAKSI (jika mau live, buka baris ini) ===
# signed = w3.eth.account.sign_transaction(tx, PRIVATE_KEY)
# tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
# print("TX BUY DIKIRIM (testnet)! Hash:", tx_hash.hex())
# w3.eth.wait_for_transaction_receipt(tx_hash)
# print("Transaksi selesai (cek explorer testnet).")

# --- CEK SALDO SESUDAH BUY (opsional) ---
# balance_after = w3.eth.get_balance(WALLET)
# print(f"Saldo setelah buy: {w3.from_wei(balance_after, 'ether')} BASE (testnet)")