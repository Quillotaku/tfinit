import sys
import os

try:
    sys.argv.index("--help")
    print("""
    Uso: python tfinit.py --help
    --files FILE_A,FILE_B,...,FILE_N: Crea N ficheros con la extension .tf de Terraform. Si el nombre es variables o backend, se genera también un fichero .tfvars.
    --env ENV_A,ENV_B,...,ENV_N: Uso complementario para ficheros variables y backend. Crea una carpeta variables y/o backend y N ficheros variables-ENV y/o backend-ENV.

    EJEMPLOS:
        python tfinit.py --files variables,backend,provider,locals,data --env des,pre,pro
        > backend
            backend-des.tfvars
            backend-pre.tfvars
            backend-pro.tfvars
          variables
            variables-des.tfvars
            variables-pre.tfvars
            variables-pro.tfvars
          backend.tf
          data.tf
          locals.tf
          provider.tf
          variables.tf

        python tfinit.py --files variables,backend,provider,locals,data
        > backend.tf
          backend.tfvars
          variables.tf
          variables.tfvars
          data.tf
          locals.tf
          provider.tf
    """,)
    sys.exit(1)
except ValueError:
    pass

for filename in sys.argv[sys.argv.index("--files") + 1].split(","):
    if filename in ["variables","backend"]:
        with open(file=f"{filename}.tf",encoding="UTF-8",mode="w") as f:
            f.write(f"//{filename}")
        try:
            for envs in sys.argv[sys.argv.index("--env") + 1].split(","):
                try:
                    os.makedirs(os.path.join(os.getcwd(),filename))
                except FileExistsError:
                    # directory already exists
                    pass
                with open(file=os.path.join(os.getcwd(),filename,f"{filename}-{envs}.tfvars"),encoding="UTF-8",mode="w") as f:
                    f.write(f"//{filename}-{envs}")
        except:
            with open(file=f"{filename}.tfvars",encoding="UTF-8",mode="w") as f:
                f.write(f"//{filename}")
    with open(file=f"{filename}.tf",encoding="UTF-8",mode="w") as f:
        f.write(f"//{filename}")