#!/usr/bin/env python

import getpass
import os


jackhmmer_binary_path = "/opt/conda/bin/jackhmmer"
hhblits_binary_path = "/opt/conda/bin/hhblits"
hhsearch_binary_path = "/opt/conda/bin/hhsearch"
kalign_binary_path = "/opt/conda/bin/kalign"
hmmsearch_binary_path = "/opt/conda/bin/hmmsearch"
hmmbuild_binary_path = "/opt/conda/bin/hmmbuild"

data_dir = "/app/alphafold_db"

# Path to the Uniref90 database for use by JackHMMER.
uniref90_database_path = os.path.join(data_dir, "uniref90", "uniref90.fasta")

# Path to the MGnify database for use by JackHMMER.
mgnify_database_path = os.path.join(data_dir, "mgnify.old", "mgy_clusters_2018_12.fa")

# Path to the BFD database for use by HHblits.
bfd_database_path = os.path.join(
    data_dir, "bfd", "bfd_metaclust_clu_complete_id30_c90_final_seq.sorted_opt"
)
small_bfd_database_path = os.path.join(
    data_dir, "small_bfd", "bfd-first_non_consensus_sequences.fasta"
)

# Path to the UniRef30 database for use by HHblits.
uniref30_database_path = os.path.join(
    data_dir, "uniclust30/uniclust30_2018_08", "uniclust30_2018_08"
)

# Path to the UniProt database for used by JackHMMer.
uniprot_database_path = os.path.join(data_dir, "uniprot", "uniprot.fasta")

# Path to the PDB70 database for use by HHsearch.
pdb70_database_path = os.path.join(data_dir, "pdb70", "pdb70")

# Path to the PDB seqres database for use by hmmsearch.
pdb_seqres_database_path = os.path.join(data_dir, "pdb_seqres", "pdb_seqres.txt")

# Path to a directory with template mmCIF structures, each named <pdb_id>.cif')
template_mmcif_dir = os.path.join(data_dir, "pdb_mmcif", "mmcif_files")

# Path to a file mapping obsolete PDB IDs to their replacements.
obsolete_pdbs_path = os.path.join(data_dir, "pdb_mmcif", "obsolete.dat")

max_template_date = "2018-04-30"
num_predictions_per_model = 50

model_preset = 'monomer'
model_names = [
    1, 
    2
]

os.environ["NVIDIA_VISIBLE_DEVICES"] = os.getenv("NVIDIA_VISIBLE_DEVICES", "")
os.environ["TF_FORCE_UNIFIED_MEMORY"] = os.getenv("TF_FORCE_UNIFIED_MEMORY")
os.environ["XLA_PYTHON_CLIENT_MEM_FRACTION"] = os.getenv(
    "XLA_PYTHON_CLIENT_MEM_FRACTION"
)

if os.getenv("NVIDIA_VISIBLE_DEVICES", "") == "":
    os.environ["JAX_PLATFORM_NAME"] = "cpu"
    os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

N_PROC = int(os.getenv("SLURM_CPUS_PER_TASK", 8))

script_home = os.path.dirname(os.path.abspath(__file__))
exec_run_alphafold = os.path.join(script_home, "run_af.py")
exec_run_tbm = os.path.join(script_home, "run_tbm.py")

gpcr100_active_db_path = "/app/alphafold-multistate/db/GPCR100.ACTIVE/GPCR100.Active"
gpcr100_inactive_db_path = (
    "/app/alphafold-multistate/db/GPCR100.INACTIVE/GPCR100.Inactive"
)

gpcr100_mmcif_active_db_path = "/app/alphafold-multistate/db/GPCR100.ACTIVE/cif.active"
gpcr100_mmcif_inactive_db_path = (
    "/app/alphafold-multistate/db/GPCR100.INACTIVE/cif.inactive"
)

kinase100_active_db_path = "/app/alphafold-multistate/db/KINASE100/kinase100.DFGin_All"
kinase100_inactive_db_path = (
    "/app/alphafold-multistate/db/KINASE100/kinase100.DFGout_All"
)

kinase100_mmcif_active_db_path = "/app/alphafold-multistate/db/KINASE100/pdb_mmcif"
kinase100_mmcif_inactive_db_path = "/app/alphafold-multistate/db/KINASE100/pdb_mmcif"
