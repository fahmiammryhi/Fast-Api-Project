from fastapi import APIRouter

router = APIRouter(prefix="/account", tags=["account"])

@router.get("/validate/{bank_code}/{account_number}")
def validate_account(bank_code: str, account_number: str):
    # Dummy response (seakan-akan dari API Flip)
    return {
        "bank_code": bank_code,
        "account_number": account_number,
        "account_name": "Budi Santoso (Dummy)",
        "status": "success"
    }
