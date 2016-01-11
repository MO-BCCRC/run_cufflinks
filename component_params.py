'''
component_params.py

created on 2 Mar 2015
@author: jrosner

'''

return_value = []

input_files  = {
                'input'         : '__REQUIRED__',
                'GTF_guide'         : None,
                'mask_file'         : None,
                'frag_bias_correct' : None,
                }

output_files = {'output_dir' : '__REQUIRED__'}

input_params = {
                'num_threads'                    : None,
                'seed'                           : None,
                'GTF'                            : '__FLAG__',
                'multi_read_correct'             : '__FLAG__',
                'library_type'                   : None,
                'library_norm_method'            : None,
                'frag_len_mean'                  : None,
                'frag_len_std_dev'               : None,
                'max_mle_iterations'             : None,
                'compatible_hits_norm'           : '__FLAG__',
                'total_hits_norm'                : True,
                'num_frag_count_draws'           : None,
                'num_frag_assign_draws'          : None,
                'max_frag_multihits'             : None,
                'no_effective_length_correction' : '__FLAG__',
                'no_length_correction'           : '__FLAG__',
                'label'                          : None,
                'min_isoform_fraction'           : None,
                'pre_mrna_fraction'              : None,
                'max_intron_length'              : None,
                'junc_alpha'                     : None,
                'small_anchor_fraction'          : None,
                'min_frags_per_transfrag'        : None,
                'overhang_tolerance'             : None,
                'max_bundle_length'              : None,
                'max_bundle_frags'               : None,
                'min_intron_length'              : None,
                'trim_3_avgcov_thresh'           : None,
                'trim_3_dropoff_frac'            : None,
                'max_multiread_fraction'         : None,
                'overlap_radius'                 : None,
                'no_faux_reads'                  : '__FLAG__',
                '3_overhang_tolerance'           : None,
                'intron_overhang_tolerance'      : None,
                'verbose'                        : '__FLAG__',
                'quiet'                          : '__FLAG__',
                'no_update_check'                : '__FLAG__',
                }

