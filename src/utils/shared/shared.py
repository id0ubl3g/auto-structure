def shared_get_current_directory():
    from src.modules.create_structure import CreateStructure
    create_structure = CreateStructure()
    current_directory = create_structure.get_current_directory()
    return current_directory