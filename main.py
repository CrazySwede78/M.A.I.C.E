```python
from models.user_input import UserInput
from models.project import Project
from models.outline import Outline
from models.part import Part
from models.step import Step
from models.merge_verify import MergeVerify
from agents.creative_writer import CreativeWriter
from agents.project_planner import ProjectPlanner
from agents.outline_creator import OutlineCreator
from agents.part_definer import PartDefiner
from agents.step_generator import StepGenerator
from agents.merger_verifier import MergerVerifier

def main():
    # Get user input
    user_input = UserInput()
    user_input.get_user_input()

    # Create a project
    project = Project(user_input)
    project_planner = ProjectPlanner(project)
    project_planner.create_project()

    # Create an outline
    outline = Outline(project)
    outline_creator = OutlineCreator(outline)
    outline_creator.create_outline()

    # Define parts
    part = Part(outline)
    part_definer = PartDefiner(part)
    part_definer.define_part()

    # Generate steps
    step = Step(part)
    step_generator = StepGenerator(step)
    step_generator.generate_step()

    # Merge and verify content
    merge_verify = MergeVerify(step)
    merger_verifier = MergerVerifier(merge_verify)
    merger_verifier.merge_verify()

    # Generate creative writing
    creative_writer = CreativeWriter(merge_verify)
    creative_writer.generate_creative_writing()

if __name__ == "__main__":
    main()
```