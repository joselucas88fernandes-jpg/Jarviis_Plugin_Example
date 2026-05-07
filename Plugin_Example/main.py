from contracts import SkillOutput


def execute(skill_input):

    text = skill_input.user_input.lower()

    return SkillOutput.ok(
        response=f"Plugin respondeu: {text}",
        actions=[],
        metadata={"plugin": "plugin_name"}
    )
