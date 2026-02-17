def create_character(name, strength, intelligence, charisma):
    # --- Name validation ---
    if not isinstance(name, str):
        return "The character name should be a string."
    
    if name == "":
        return "The character should have a name."
    
    if len(name) > 10:
        return "The character name is too long."
    
    if " " in name:
        return "The character name should not contain spaces."
    
    
    # --- Stats type validation ---
    if not all(isinstance(stat, int) for stat in (strength, intelligence, charisma)):
        return "All stats should be integers."
    
    
    # --- Stats range validation ---
    if any(stat < 1 for stat in (strength, intelligence, charisma)):
        return "All stats should be no less than 1."
    
    if any(stat > 4 for stat in (strength, intelligence, charisma)):
        return "All stats should be no more than 4."
    
    
    # --- Total points validation ---
    if strength + intelligence + charisma != 7:
        return "The character should start with 7 points."
    
    
    # --- Build character sheet ---
    def build_stat_line(label, value):
        full = "●" * value
        empty = "○" * (10 - value)
        return f"{label} {full}{empty}"
    
    result = (
        f"{name}\n"
        f"{build_stat_line('STR', strength)}\n"
        f"{build_stat_line('INT', intelligence)}\n"
        f"{build_stat_line('CHA', charisma)}"
    )
    
    return result
