class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        k = ""
        for a in self.authors:
            k += f"\n- {a}"
        
        r = ""
        for d in self.dependencies:
            r += f"\n- {d}"

        kk = ""
        for dd in self.dev_dependencies:
            kk += f"\n- {dd}"

        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nlicense: {self.license}\n"
            f"\nAuthors: {k}\n"
            f"\nDependencies: {r}\n"
            f"\nDevelopment dependencies: {kk}"
        )
