from langchain.tools import tool
import pandas as pd
from pathlib import Path

CSV_PATH = Path(__file__).parent / "candidates.csv"
leave_requests = {}

def load_candidates():
    return pd.read_csv(CSV_PATH)

def save_candidates(df):
    df.to_csv(CSV_PATH, index=False)

@tool
def get_candidate_info(name: str) -> str:
    """Get info about a candidate by name."""
    df = load_candidates()
    row = df[df["name"].str.lower() == name.strip().lower()]
    if not row.empty:
        r = row.iloc[0]
        return f"""
Name: {r['name']}
Email: {r['email']}
Skills: {r['skills']}
Status: {r['status']}
Experience: {r['experience']} years
Department: {r['department']}
Location: {r['location']}
""".strip()
    return f"No candidate found with name: {name}"

@tool
def schedule_interview(input_str: str) -> str:
    """Schedule interview. Format: Name | Date | Time"""
    try:
        name, date, time = input_str.split("|")
        name, date, time = name.strip(), date.strip(), time.strip()

        df = load_candidates()
        if name in df["name"].values:
            return f"Interview scheduled with {name} on {date} at {time}."
        return f"Candidate {name} not found."
    except:
        return "Invalid format. Use: Name | Date | Time"


@tool
def update_candidate_status(input_str: str) -> str:
    """Update status. Format: Name | NewStatus"""
    try:
        name, status = input_str.split("|")
        name, status = name.strip(), status.strip()
        df = load_candidates()
        if name in df["name"].values:
            df.loc[df["name"] == name, "status"] = status
            save_candidates(df)
            return f"{name}'s status updated to {status}."
        return f"Candidate {name} not found."
    except:
        return "Invalid format. Use: Name | NewStatus"

@tool
def list_candidates_by_skill(skill: str) -> str:
    """List candidates by skill keyword."""
    df = load_candidates()
    filtered = df[df["skills"].str.contains(skill.strip(), case=False)]
    if not filtered.empty:
        return "Matching candidates: " + ", ".join(filtered["name"])
    return f"No candidates found with skill: {skill}"

@tool
def remove_candidate(name: str) -> str:
    """Remove a candidate by name."""
    df = load_candidates()
    if name.strip() in df["name"].values:
        df = df[df["name"] != name.strip()]
        save_candidates(df)
        return f"Candidate {name} removed."
    return f"Candidate {name} not found."

@tool
def apply_leave(input_str: str) -> str:
    """Apply leave. Format: Name | Date | Reason"""
    try:
        name, date, reason = input_str.split("|")
        name, date, reason = name.strip(), date.strip(), reason.strip()
        if name not in leave_requests:
            leave_requests[name] = []
        leave_requests[name].append({"date": date, "reason": reason, "status": "Pending"})
        return f"Leave submitted for {name} on {date} (Reason: {reason})"
    except:
        return "Invalid format. Use: Name | Date | Reason"

@tool
def check_leave_status(name: str) -> str:
    """Check leave status."""
    if name not in leave_requests or not leave_requests[name]:
        return f"No leave requests for {name}."
    return "\\n".join([f"{r['date']} - {r['reason']} - {r['status']}" for r in leave_requests[name]])

@tool
def approve_leave(input_str: str) -> str:
    """Approve leave. Format: Name | Date"""
    try:
        name, date = input_str.split("|")
        name, date = name.strip(), date.strip()
        for r in leave_requests.get(name, []):
            if r["date"] == date:
                r["status"] = "Approved"
                return f"Leave for {name} on {date} approved."
        return f"No leave request for {name} on {date}."
    except:
        return "Invalid format. Use: Name | Date"

@tool
def reject_leave(input_str: str) -> str:
    """Reject leave. Format: Name | Date"""
    try:
        name, date = input_str.split("|")
        name, date = name.strip(), date.strip()
        for r in leave_requests.get(name, []):
            if r["date"] == date:
                r["status"] = "Rejected"
                return f"Leave for {name} on {date} rejected."
        return f"No leave request for {name} on {date}."
    except:
        return "Invalid format. Use: Name | Date"
